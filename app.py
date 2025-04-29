# Import necessary libraries

import streamlit as st
import os
from openai import OpenAI
import json

working_dir = os.path.dirname(os.path.abspath(__file__))
endpoint_data = json.load(open(f"{working_dir}/model_info.json"))

def clear_chat():
    st.session_state.messages = []

st.title("Intel® AI for Enterprise Inference")
st.header("LLM chatbot")

# Extract the keys (model names) from the JSON data
# model_names = list(endpoint_data.keys())


with st.sidebar:
    #Enter openai_api key under "Secrets " in HF settings
    #Enter base_url under "Variables" in HF settings
    api_key = st.session_state.api_key = st.secrets["openai_apikey"]
    base_url = st.session_state.base_url = os.environ.get("base_url")
    client = OpenAI(api_key=api_key, base_url=base_url)
    models = client.models.list()
    model_names = sorted([model.id for model in models])  # Extract 'id' from each model object
    # Specify the default model name
    default_model_name = "meta-llama/Llama-3.3-70B-Instruct"  # Replace with your desired default model name
    
    
    # Use st.session_state to persist the selected model
    if "selected_model" not in st.session_state:
        # st.session_state.selected_model = model_names[0]  # Default to the first model
        st.session_state.selected_model = default_model_name if default_model_name in model_names else model_names[0]

    modelname = st.selectbox(
        "Select LLM model (Running on Intel® Gaudi®) on Denvr Dataworks",
        model_names,
        index=model_names.index(st.session_state.selected_model) if st.session_state.selected_model in model_names else 0,
        key="selected_model",
    )
    st.write(f"You selected: {modelname}")
    st.button("Start New Chat", on_click=clear_chat)
    
try:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                stream = client.chat.completions.create(
                    model=modelname,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    max_tokens=4096,
                    stream=True,
                )
                response = st.write_stream(stream)
            except Exception as e:
                st.error(f"An error occurred while generating the response: {e}")
                response = "An error occurred while generating the response."

        st.session_state.messages.append({"role": "assistant", "content": response})
except KeyError as e:
    st.error(f"Key error: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")