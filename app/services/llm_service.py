import asyncio
import ollama
from app.config import Config
from app.utils.prompt_builder import build_explanation_prompt, build_fallback_explanation

async def generate_advice(label: str, confidence: float) -> str:
    """
    Menghasilkan saran penanganan menggunakan Ollama berdasarkan hasil deteksi CV.
    
    Args:
        label: Kelas penyakit dari Roboflow
        confidence: Tingkat keyakinan prediksi
        
    Returns:
        String respons dalam format Markdown
    """
    # 1. Rakit prompt menggunakan utility yang sudah dibuat
    prompt = build_explanation_prompt(label, confidence)
    
    try:
        # 2. Panggil Ollama secara asynchronous dengan parameter temperature dari config
        response = await asyncio.to_thread(
            ollama.generate,
            model=Config.LLM_MODEL,
            prompt=prompt,
            options={"temperature": Config.TEMPERATURE},
            stream=False
        )
        
        # 3. Kembalikan teks respons dari LLM
        return response.get("response", build_fallback_explanation(label, confidence))
        
    except Exception as e:
        print(f"[Error LLM Service]: Ollama gagal merespons. Detail: {str(e)}")
        # Jika Ollama down atau model belum di-pull, gunakan pesan fallback
        return build_fallback_explanation(label, confidence)