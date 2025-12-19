import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    RBF_API_URL = os.getenv("RBF_API_URL", "https://serverless.roboflow.com")
    RBF_API_KEY = os.getenv("RBF_API_KEY", "58c7Qs0Cbmt5M5MvbPXk")
    RBF_MODEL = os.getenv("RBF_MODEL", "palm-tree-leaves-diseases-old/2")

    LLM_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))
    SYSTEM_PROMPT_HEALTHY = os.getenv("SYSTEM_PROMPT_HEALTHY")
    PROMPT_TEMPLATE_DISEASE = os.getenv("SYSTEM_PROMPT_DISEASE")