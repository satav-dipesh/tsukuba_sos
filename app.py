import streamlit as st
import os
from openai import OpenAI
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def clear_chat():
    st.session_state.messages = []

def initialize_provider_settings(provider_choice):
    """Configure API settings based on provider selection"""
    provider_configs = {
        "Hugging Face": {
            "api_key_source": os.environ.get("HUGGINGFACE_API_KEY", ""),
            "base_url_source": "https://router.huggingface.co/v1/",
            "fallback_model": "meta-llama/Llama-3.2-3B-Instruct"
        },
        "IBM": {
            "api_key_source": os.environ.get("ibm_openai_apikey", ""),
            "base_url_source": os.environ.get("ibm_base_url", ""),
            "fallback_model": None
        }
    }
    
    return provider_configs.get(provider_choice, {})

st.title("Tsukuba SOS")
st.header("LLM chatbot")

with st.sidebar:
    # Provider selection dropdown
    available_providers = ["Hugging Face", "IBM"]
    
    if "current_provider_choice" not in st.session_state:
        st.session_state.current_provider_choice = available_providers[0]
    
    provider_selection = st.selectbox(
        "Choose AI Provider:",
        available_providers,
        key="current_provider_choice"
    )
    
    # Get provider-specific settings
    provider_settings = initialize_provider_settings(provider_selection)
    
    # Validate required credentials
    if not provider_settings.get("api_key_source") or not provider_settings.get("base_url_source"):
        st.error(f"Configuration missing for {provider_selection}. Check environment variables.")
        st.stop()
    
    # Setup OpenAI client
    try:
        api_client = OpenAI(
            api_key=provider_settings["api_key_source"], 
            base_url=provider_settings["base_url_source"]
        )
        available_models = api_client.models.list()
        model_list = sorted([m.id for m in available_models])
        
        # Handle model selection with provider switching
        session_key = f"model_for_{provider_selection}"
        if session_key not in st.session_state or st.session_state.get("last_provider") != provider_selection:
            preferred_model = provider_settings.get("fallback_model")
            if preferred_model and preferred_model in model_list:
                st.session_state[session_key] = preferred_model
            elif model_list:
                st.session_state[session_key] = model_list[0]
            st.session_state.last_provider = provider_selection
        
        if not model_list:
            st.error(f"No models found for {provider_selection}")
            st.stop()
        
        # Model selection interface
        chosen_model = st.selectbox(
            f"Available models from {provider_selection}:",
            model_list,
            key=session_key,
        )
        st.info(f"Active model: {chosen_model}")
        
    except Exception as connection_error:
        st.error(f"Connection failed for {provider_selection}: {connection_error}")
        st.stop()
    
    st.button("Reset Conversation", on_click=clear_chat)
    
    st.markdown("---")
    
    # Display provider-specific information
    if provider_selection == "Hugging Face":
        st.markdown(
            """
            **Hugging Face Integration**
            
            Using models from [Hugging Face](https://huggingface.co/) for testing.
            
            Get your API token at: [HF Settings](https://huggingface.co/settings/tokens)
            
            Set environment variable: `HUGGINGFACE_API_KEY`
            """
        )
    elif provider_selection == "IBM":
        st.markdown(
            """
            **IBM AI Services**
            
            Connected to IBM's AI infrastructure. Ensure your credentials are properly configured.
            """
        )

# Main chat interface
try:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display conversation history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle new user input
    if user_input := st.chat_input("Enter your message..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate AI response
        with st.chat_message("assistant"):
            try:
                response_stream = api_client.chat.completions.create(
                    model=chosen_model,
                    messages=[
                        {"role": msg["role"], "content": msg["content"]}
                        for msg in st.session_state.messages
                    ],
                    max_tokens=4096,
                    stream=True,
                )
                ai_response = st.write_stream(response_stream)
            except Exception as generation_error:
                st.error(f"Response generation failed: {generation_error}")
                ai_response = "Unable to generate response due to an error."

        st.session_state.messages.append({"role": "assistant", "content": ai_response})

except KeyError as key_err:
    st.error(f"Configuration key error: {key_err}")
except Exception as general_err:
    st.error(f"Unexpected error occurred: {general_err}")