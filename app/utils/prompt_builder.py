def get_confidence_level(confidence: float) -> str:
    """
    Mengonversi nilai numerik confidence menjadi tingkat keyakinan yang mudah dibaca.
    
    Args:
        confidence: Float antara 0 dan 1
        
    Returns:
        Deskripsi tingkat keyakinan (String)
    """
    if confidence >= 0.85:
        return "Sangat meyakinkan"
    elif confidence >= 0.70:
        return "Kemungkinan besar"
    elif confidence >= 0.50:
        return "Indikasi awal"
    else:
        return "Tidak pasti, perlu verifikasi lanjutan"


def build_explanation_prompt(label: str, confidence: float) -> str:
    """
    Membangun prompt terstruktur untuk penjelasan LLM.
    
    Args:
        label: Kelas penyakit yang terdeteksi
        confidence: Tingkat keyakinan prediksi (0-1)
        
    Returns:
        String prompt yang sudah diformat untuk LLM
    """
    confidence_level = get_confidence_level(confidence)
    confidence_pct = confidence * 100
    
    prompt = f"""Anda adalah pakar agronomi kelapa sawit berpengalaman. Tolong berikan penjelasan profesional mengenai kondisi berikut:
    
HASIL DETEKSI:
- Kondisi: {label}
- Tingkat Keyakinan: {confidence_pct:.1f}% ({confidence_level})

INSTRUKSI:
Berikan respons dalam format berikut (BAHASA INDONESIA):

1. PENJELASAN KONDISI (2-3 kalimat singkat):
- Jelaskan apa itu {label}
- Sebutkan penyebab umumnya

2. TINDAKAN YANG DISARANKAN (3-4 poin):
- Tindakan segera yang harus dilakukan
- Langkah-langkah perawatan atau pengendalian
- JANGAN sebutkan dosis bahan kimia spesifik atau merek dagang

3. PENCEGAHAN (2-3 poin):
- Cara mencegah kondisi ini terulang di masa depan

PENTING:
- Gunakan bahasa yang mudah dipahami oleh petani
- Jangan berikan informasi di luar domain pertanian kelapa sawit
- Jika tingkat keyakinan rendah (<50%), sertakan saran wajib untuk berkonsultasi dengan ahli/PPL (Penyuluh Pertanian Lapangan)
- Fokus pada praktik pertanian yang baik (Good Agricultural Practices), bukan promosi produk komersial
- Gunakan format Markdown untuk kerapian.

Jawablah dengan profesional, praktis, dan solutif."""
    
    return prompt


def build_fallback_explanation(label: str, confidence: float) -> str:
    """
    Menghasilkan penjelasan cadangan (fallback) ketika LLM gagal merespons.
    
    Args:
        label: Kelas penyakit yang terdeteksi
        confidence: Tingkat keyakinan prediksi (0-1)
        
    Returns:
        Penjelasan cadangan yang aman
    """
    confidence_level = get_confidence_level(confidence)
    
    return f"""**Kondisi terdeteksi:** {label}
**Tingkat keyakinan:** {confidence*100:.1f}% ({confidence_level})

*Penjelasan otomatis dari AI saat ini tidak tersedia.* Harap segera konsultasikan temuan ini dengan pakar agronomi atau petugas penyuluh lapangan terdekat untuk analisis lebih lanjut. Untuk informasi umum mengenai kondisi **{label}**, Anda dapat merujuk pada buku panduan teknis budidaya kelapa sawit dari instansi pertanian resmi."""