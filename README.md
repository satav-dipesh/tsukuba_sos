---
title: Intel® AI for Enterprise Inference
emoji: 📚
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.45.1
app_file: app.py
pinned: false
license: apache-2.0
short_description: 'LLM Chatbot on Denvr Dataworks and Intel Gaudi'
---

# LLM Chatbot
Similar to ChatGPT, this application provides a user-friendly Streamlit interface to interact with various LLM models hosted on Denvr Dataworks, powered by Intel Gaudi accelerators. The chatbot supports streaming responses and offers a selection of different language models, including Llama, DeepSeek, and Qwen models. Try it yourself with the models available in the left drop-down menu. 

[![llmchatbot](images/llmchatbot.png)](https://huggingface.co/spaces/Intel/intel-ai-enterprise-inference)

## Setup

If you want to hose the application locally with Streamlit, you can follow the steps below. If you want to host the application on Hugging Face Spaces, the easiest way is to duplicate the space as per the screenshot, and set up your own API secrets as detailed below. Just like any GitHub repository, you can use the same Git actions with the Hugging Face Space to clone, add, push, and commit your changes.

[![hf_dup](images/hf_dup.png)](https://huggingface.co/spaces/Intel/intel-ai-enterprise-inference)

1. Clone the repository:
```bash
git clone https://huggingface.co/spaces/Intel/intel-ai-enterprise-inference
cd intel-ai-enterprise-inference
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Secrets Management

This application requires API credentials to be set up in Streamlit's secrets management. You need an OpenAI-compatible API key. In the case of this application, it is using an API key from [Denvr Dataworks](https://www.denvrdata.com/intel).

1. On Hugging Face Spaces:
- Add your OpenAI-compatible API key under "Secrets" in the HF settings as `openai_apikey`
- Add the base URL for your model endpoint under "Variables" as `base_url`

2. For local development, create a `.streamlit/secrets.toml` file with:
```toml
openai_apikey = "your-api-key-here"
```
Set the `base_url` environment variable to point to your OpenAI-compliant model endpoint with hosted models.
```bash
export base_url="https://api.inference.denvrdata.com/v1/"
```
Run the Streamlit application locally:

```bash
streamlit run app.py
```

## Follow Up

Connect to LLMs on Intel® Gaudi® accelerators with just an endpoint and an OpenAI-compatible API key, courtesy of cloud-provider Denvr Dataworks: https://www.denvrdata.com/intel

Chat with 6K+ fellow developers on the Intel DevHub Discord: https://discord.gg/kfJ3NKEw5t

Connect with me on LinkedIn: https://linkedin.com/in/bconsolvo


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
