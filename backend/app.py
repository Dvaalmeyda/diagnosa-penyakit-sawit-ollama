from main import SawitDiseaseAI
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()
ai_system = SawitDiseaseAI()

@app.get("/")
async def root():
    return {"message": "Sawit Disease AI is running."}

@app.post("/analyze-image/")
async def analyze_image(file: UploadFile = File(...)):
    image = await file.read()
    nama_penyakit = ai_system.analyze_image(image)

    disease_info = ai_system.get_disease_info(nama_penyakit)
        
    return {
        "detected_disease": nama_penyakit,
        "disease_information": disease_info
    }