# ©2024 Intel Corporation
# Permission is granted for recipient to internally use and modify this software for purposes of benchmarking and testing on Intel architectures. 
# This software is provided "AS IS" possibly with faults, bugs or errors; it is not intended for production use, and recipient uses this design at their own risk with no liability to Intel.
# Intel disclaims all warranties, express or implied, including warranties of merchantability, fitness for a particular purpose, and non-infringement. 
# Recipient agrees that any feedback it provides to Intel about this software is licensed to Intel for any purpose worldwide. No permission is granted to use Intel’s trademarks.
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the code.

# Import necessary libraries

import streamlit as st
import os
from openai import OpenAI
import json



working_dir = os.path.dirname(os.path.abspath(__file__))
endpoint_data = json.load(open(f"{working_dir}/model_info.json"))

def clear_chat():
    st.session_state.messages = []

st.title("Chat Bot")

# Extract the keys (model names) from the JSON data
model_names = list(endpoint_data.keys())

with st.sidebar:
    modelname = st.selectbox("Select a LLM model (Hosted by DENVR DATAWORKS) ", model_names)
    st.write(f"You selected: {modelname}")
    st.button("Start New Chat", on_click=clear_chat)

endpoint = endpoint_data[modelname]
    
# api_key=os.environ.get('API_KEY')
api_key = st.secrets["openai_apikey"]

if not api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()
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
        stream = client.chat.completions.create(
            model=modelname,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens=5000,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


