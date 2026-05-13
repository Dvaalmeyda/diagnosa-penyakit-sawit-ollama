from main import SawitAI
from fastapi import FastAPI, HTTPException

app = FastAPI()
sawit_ai = SawitAI()

# Get list of diseases
@app.get("/diseases")
async def get_diseases_list():
    return {
        "total diseases": len(sawit_ai.penyakit_list),
        "diseases": sawit_ai.penyakit_list
    }

# Get disease information by ID
@app.get("/disease/{disease_id}")
async def get_disease_info(disease_id: int):
    # Validate disease ID
    if disease_id not in sawit_ai.penyakit_list:
        raise HTTPException(status_code=404, detail="Disease not found.")
    
    # Response
    disesase_info = sawit_ai.get_penyakit_info(disease_id)
    return {
        "disease_id": disease_id,
        "disease_name": sawit_ai.penyakit_list[disease_id],
        "information": disesase_info
    }

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the SawitAI Disease Diagnosis API. Use /diseases to get the list of diseases."}
