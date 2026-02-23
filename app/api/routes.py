import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.cv_service import predict_disease  
from app.services.llm_service import generate_advice 
from app.utils.prompt_builder import build_explanation_prompt
from app.schemas.prediction import ClassificationResult, ExplanationResponse

router = APIRouter()

@router.get("/health")
def health_check():
    """Endpoint untuk mengecek apakah server berjalan."""
    return {"status": "ok", "message": "Palm Disease API is running."}

@router.post("/predict-image", response_model=ClassificationResult)
async def predict_image(file: UploadFile = File(...)):
    """
    Endpoint CV only. Menerima gambar dan mengembalikan hasil klasifikasi.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File harus berupa gambar.")

    temp_file_path = f"temp_{file.filename}"
    
    try:
        # Simpan file sementara
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Panggil CV Service (fungsi predict_disease yang kita buat sebelumnya)
        result = await predict_disease(temp_file_path)
        
        # Perhatikan: Sesuaikan 'label' karena sebelumnya kita pakai key 'class' di dict
        return ClassificationResult(
            label=result["class"], 
            confidence=result["confidence"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CV Error: {str(e)}")
        
    finally:
        # Hapus file setelah selesai agar storage tidak penuh
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@router.post("/explain-result", response_model=ExplanationResponse)
async def explain_result(result: ClassificationResult):
    """
    Endpoint LLM only. Menerima JSON hasil klasifikasi dan mengembalikan penjelasan.
    """
    try:
        # Karena di llm_service.py kita sudah memanggil prompt_builder di dalam fungsinya,
        # kita cukup mengirim label dan confidence ke service tersebut.
        explanation_text = await generate_advice(
            label=result.label, 
            confidence=result.confidence
        )

        return ExplanationResponse(
            classification=result,
            explanation=explanation_text
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")