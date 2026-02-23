from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

# Inisialisasi aplikasi FastAPI beserta metadatanya untuk Swagger UI
app = FastAPI(
    title="Palm Oil Disease AI Service",
    description="API untuk deteksi penyakit daun kelapa sawit menggunakan Computer Vision (Roboflow) dan Generative AI (Ollama).",
    version="1.0.0"
)

# Konfigurasi CORS agar API bisa diakses dari aplikasi Web/Mobile (Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Saat production, ganti "*" dengan URL domain frontend kamu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mendaftarkan semua endpoint dari routes.py
# Menambahkan prefix /api/v1 adalah best practice untuk versioning API
app.include_router(router, prefix="/api/v1")