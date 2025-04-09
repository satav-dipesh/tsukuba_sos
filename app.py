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
model_names = list(endpoint_data.keys())


with st.sidebar:
    modelname = st.selectbox("Select a LLM model (Running on Intel® Gaudi®) ", model_names)
    st.write(f"You selected: {modelname}")
    st.button("Start New Chat", on_click=clear_chat)
    try:
        #if you can provide the API key in the HF settings under "Variables and secrets", you will not need to enter your OpenAI-compatible API key every time.
        st.session_state.api_key = st.secrets["openai_apikey"]
    except KeyError:
    # Add a text input for the API key if not in session state
        api_key = st.text_input("Enter your API Key", type="password")
        if api_key:
            st.session_state.api_key = api_key    

# Check if the API key is provided
if "api_key" not in st.session_state or not st.session_state.api_key:
    st.error("Please enter your API Key in the sidebar.")
else:
    try:
        endpoint = endpoint_data[modelname]
        
        api_key = st.session_state.api_key
        base_url = endpoint
        client = OpenAI(api_key=api_key, base_url=base_url)

        # Extract the model name
        models = client.models.list()
        modelname = models.data[0].id

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