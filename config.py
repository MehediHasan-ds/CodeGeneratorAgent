# config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_ID = os.getenv("MODEL_ID", "llama3-8b-8192")
    MAX_TOKENS = 1500
    TEMPERATURE = 0.5
