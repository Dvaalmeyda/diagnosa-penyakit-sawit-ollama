import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))
    PROMPT_TEMPLATE = os.getenv("SYSTEM_PROMPT")