# Dynamic - Research Paper Summarizer

A Streamlit-based web application that summarizes research papers using LangChain and the Groq LLM API.

## Features

- **Multiple Research Papers**: Choose from classic AI/ML papers:
  - Attention Is All You Need
  - BERT: Pre-training of Deep Bidirectional Transformers
  - GPT-3: Language Models are Few-Shot Learners
  - Diffusion Models Beat GANs on Image Synthesis

- **Customizable Explanations**: Select your preferred explanation style:
  - Beginner-Friendly
  - Technical
  - Code-Oriented
  - Mathematical

- **Flexible Summary Length**: Choose how detailed you want the summary:
  - Short (1-2 paragraphs)
  - Medium (3-5 paragraphs)
  - Long (detailed explanation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhushanpatil876/Dynamic.git
cd Dynamic
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

Get your API key from [Groq Console](https://console.groq.com)

## Usage

Run the Streamlit application:
```bash
streamlit run LLM/dynamic.py
```

The application will open in your browser. Select your desired research paper, explanation style, and length, then click "Summarize" to get your customized summary.

## Requirements

- Python 3.8+
- langchain-core
- langchain-groq
- python-dotenv
- streamlit

See `requirements.txt` for all dependencies.

## Technologies Used

- **Streamlit**: Interactive web framework
- **LangChain**: LLM framework for building AI applications
- **Groq**: Fast LLM inference API
- **Python-dotenv**: Environment variable management

## License

This project is open source and available under the MIT License.

## Author

[bhushanpatil876](https://github.com/bhushanpatil876)
