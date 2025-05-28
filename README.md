---
title: Intel® AI for Enterprise Inference
emoji: 📚
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: 'LLM Chatbot on Denvr Dataworks and Intel Gaudi'
---

# LLM Chat App

This application provides a user-friendly interface to interact with various LLM models hosted on Denvr Dataworks, powered by Intel Gaudi accelerators. The chatbot supports streaming responses and offers a selection of different language models, including Llama models and DeepSeek models.

## Features

- **Model Selection**: Choose from multiple LLM models hosted on Intel Gaudi hardware
- **Chat Interface**: Clean and intuitive Streamlit chat UI
- **Streaming Responses**: Real-time streaming of AI-generated responses, including formatted code blocks if requested
- **Conversation History**: Maintain context throughout your conversation
- **New Chat**: Option to start a fresh conversation at any time

## Installation

### Prerequisites

- Python 3.7+
- Streamlit
- OpenAI-compatible API key and endpoint

### Setup

1. Clone the repository:
   ```bash
git clone https://github.com/opea-project/Enterprise-Inference/
cd examples/chatapp
   ```

2. Install the required packages:
   ```bash
pip install -r requirements.txt
   ```

## Configuration

### Secrets Management

This application requires API credentials to be set up in Streamlit's secrets management:

1. On Hugging Face Spaces:
   - Add your OpenAI-compatible API key under "Secrets" in the HF settings
   - Add the base URL for your model endpoint under "Variables" as `base_url`

2. For local development:
   - Create a `.streamlit/secrets.toml` file with:
     ```toml
openai_apikey = "your-api-key-here"
     ```
   - Set the `base_url` environment variable to point to your model endpoint with hosted models.

## Running the Application

### On Hugging Face Spaces

You can create a new Hugging Face Space [here](https://huggingface.co/new-space), and then use git operations to clone, commit, and push your code changes directly to your Space. Here is the live link to the Space that you can replicate: 
https://huggingface.co/spaces/Intel/intel-ai-enterprise-inference. 

### Local Development

Run the Streamlit application locally:

```
streamlit run app.py
```


## Using the Chatbot

1. Select your desired LLM model from the dropdown menu
2. Type your message in the chat input field
3. View the AI's response as it streams in real-time
4. Continue the conversation or start a new chat using the "Start New Chat" button

## Getting API Access

To use this application, you need an OpenAI-compatible API key from Denvr Dataworks:

1. Visit [Denvr Dataworks](https://www.denvrdata.com/intel) to check the latest available models
2. Sign up for API access to receive your API key
3. Configure the key in your Streamlit secrets

## Troubleshooting

- **API Key Issues**: Ensure your API key is correctly set in the Streamlit secrets
- **Model Unavailability**: If a model is not responding, try selecting a different model
- **Error Messages**: Check the error output for specific API or connection issues
- **Rate Limiting**: You might encounter rate limits depending on your API plan

## Community and Support

Join other AI developers on [Intel's DevHub Discord server](https://discord.gg/kfJ3NKEw5t) for discussions, support, and updates.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
