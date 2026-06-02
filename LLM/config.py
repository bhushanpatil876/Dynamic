import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"

# Application Settings
MAX_SUMMARY_LENGTH = 5000
CACHE_ENABLED = True
CACHE_DIR = "cache"

# UI Settings
APP_TITLE = "Research Tool"
APP_DESCRIPTION = "AI Research Paper Summarizer"

# Validation
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please create a .env file with your API key.")
