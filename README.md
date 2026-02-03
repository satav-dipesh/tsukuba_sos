# Tsukuba SOS - Second Opinion System

A medical AI chatbot system developed in collaboration with the University of Tsukuba Medical Hospital to provide second opinion support for bladder cancer cases.

## Overview

Tsukuba SOS (Second Opinion System) is an AI-powered medical consultation tool designed to assist healthcare professionals in evaluating bladder cancer cases. The system leverages fine-tuned large language models trained on comprehensive bladder cancer guidelines to provide informed second opinions.

## Features

- 🏥 **Medical-Grade AI**: Fine-tuned models specifically trained on bladder cancer clinical guidelines
- 💬 **Interactive Chat Interface**: Easy-to-use conversational interface for medical consultations
- 🔄 **Multiple Model Support**: Flexible architecture supporting various LLM providers
- 🔐 **Secure**: Environment-based configuration for API keys and sensitive data
- 📊 **Research-Oriented**: Built for clinical research and validation in partnership with medical professionals

## Current Status

The system is currently under active development and model fine-tuning. We are:
- Training models on bladder cancer clinical guidelines
- Validating outputs with medical professionals at University of Tsukuba Medical Hospital
- Refining the system for clinical research applications

## Installation

### Prerequisites
- Python 3.9 or higher
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/cyber-medicine-cvlab/tsukuba_sos.git
   cd tsukuba_sos
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_token_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will be available at `http://localhost:8501`

## Configuration

### Hugging Face Setup

1. Create an account at [Hugging Face](https://huggingface.co/)
2. Generate an API token at [Settings → Tokens](https://huggingface.co/settings/tokens)
3. Add the token to your `.env` file

### Model Selection

The system currently supports models through:
- **Hugging Face**: Access to fine-tuned medical models and general LLMs
- **IBM**: Enterprise AI services (optional)

## Project Structure

```
tsukuba_sos/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in git)
├── .env.example       # Template for environment variables
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Research Collaboration

This project is developed in collaboration with:
- **University of Tsukuba Medical Hospital**
- **Cyber Medicine Computer Vision Lab**

The system is designed to support clinical research and is being validated with medical professionals specializing in bladder cancer treatment.

## Disclaimer

⚠️ **Important**: This system is intended for research purposes and as a supportive tool for medical professionals. It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment. All medical decisions should be made in consultation with qualified healthcare providers.

## Contributing

This is an active research project. If you're interested in contributing or collaborating, please contact the research team.

## License

See [LICENSE](LICENSE) file for details.

## Contact

For research inquiries or collaboration opportunities, please reach out through the University of Tsukuba Cyber Medicine Computer Vision Lab.

---

**Note**: This system is under active development. Models and features are continuously being improved based on clinical validation and research findings.
