import os
from dotenv import load_dotenv

# Mencari secara absolut file .env yang ada di luar folder 'app'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Muat file .env
load_dotenv(ENV_PATH)

class Config:
    RBF_API_URL = os.getenv("RBF_API_URL", "https://detect.roboflow.com")
    
    # Jika RBF_API_KEY tidak ditemukan, aplikasi akan melempar error di awal
    # sehingga kamu langsung tahu kalau .env belum disetting
    RBF_API_KEY = os.getenv("RBF_API_KEY")
    if not RBF_API_KEY:
        raise ValueError("CRITICAL: RBF_API_KEY tidak ditemukan di environment atau file .env!")

    CV_MODEL = os.getenv("RBF_MODEL", "palm-tree-leaves-diseases-old/2")

    LLM_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))