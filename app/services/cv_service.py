import asyncio
from inference_sdk import InferenceHTTPClient
from app.config import Config

# Inisialisasi client Roboflow menggunakan kredensial dari config
client = InferenceHTTPClient(
    api_url=Config.RBF_API_URL,
    api_key=Config.RBF_API_KEY
)

async def predict_disease(image_path: str) -> dict:
    """
    Mengirim gambar ke Roboflow dan mengembalikan hasil prediksi tertinggi.
    
    Args:
        image_path: Path lokal dari gambar yang akan dianalisis
        
    Returns:
        Dictionary berisi 'class' dan 'confidence'
    """
    try:
        # Menjalankan proses HTTP sinkron di background thread
        result = await asyncio.to_thread(
            client.infer, 
            image_path, 
            model_id=Config.CV_MODEL
        )
        
        # Jika tidak ada penyakit yang terdeteksi, asumsikan sehat
        if not result or "predictions" not in result or len(result["predictions"]) == 0:
            return {"class": "Healthy", "confidence": 1.0}
        
        # Ambil prediksi dengan nilai confidence paling tinggi
        top_prediction = max(result["predictions"], key=lambda x: x["confidence"])
        
        return {
            "class": top_prediction["class"],
            "confidence": top_prediction["confidence"]
        }
        
    except Exception as e:
        print(f"[Error CV Service]: {str(e)}")
        # Jika API Roboflow gagal (misal kuota habis/koneksi putus), kembalikan nilai aman
        return {"class": "Unknown API Error", "confidence": 0.0}