from inference_sdk import InferenceHTTPClient
import ollama
import cv2
import numpy as np
from config import Config

class SawitDiseaseAI:
    def __init__(self):
        self.client = InferenceHTTPClient(
            api_url=Config.RBF_API_URL,
            api_key=Config.RBF_API_KEY
        )
        self.llm_client = ollama.Client()

    def analyze_image(self, image):
        np_array = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        result = self.client.infer(img, model_id=Config.RBF_MODEL)
        nama_penyakit = result['predictions'][0]['class'].split('. ')[-1]
        return nama_penyakit

    def get_disease_info(self, nama_penyakit):
        if nama_penyakit.lower() == "healthy":
            prompt = Config.SYSTEM_PROMPT_HEALTHY
        else:
            prompt = Config.PROMPT_TEMPLATE_DISEASE.format(nama_penyakit=nama_penyakit)

        response = self.llm_client.chat(
            model=Config.LLM_MODEL, 
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": Config.TEMPERATURE,}
        )
        return response["message"]["content"]
    
# Main execution
if __name__ == "__main__":
    ai_system = SawitDiseaseAI()
    image_path = "resources/citra/fusarium_wilt.jpg"
    
    nama_penyakit = ai_system.analyze_image(image_path)
    if nama_penyakit:
        print(f"Detected Disease: {nama_penyakit}")
        disease_info = ai_system.get_disease_info(nama_penyakit)
        print("Disease Information:")
        print(disease_info)