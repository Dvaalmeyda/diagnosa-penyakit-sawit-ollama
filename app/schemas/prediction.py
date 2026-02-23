from pydantic import BaseModel, Field

class ClassificationResult(BaseModel):
    label: str = Field(..., description="Nama kelas penyakit yang terdeteksi")
    confidence: float = Field(..., description="Nilai keyakinan prediksi (0.0 - 1.0)")

class ExplanationResponse(BaseModel):
    classification: ClassificationResult
    explanation: str = Field(..., description="Penjelasan dan saran dalam format Markdown")