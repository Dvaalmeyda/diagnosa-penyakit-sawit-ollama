import ollama

client = ollama.Client()

model = "gemma3:1b"
penyakit = {
    0: "Busuk Pangkal Batang", 
    1: "Karat Daun", 
    2: "Antraknosa", 
    3: "Layu Fusarium",
    4: "Healthy"
}

print("Daftar Penyakit Tanaman Sawit:")
for key, value in penyakit.items():
    print(f"{key}: {value}")

input_text = input("Pilih nomor penyakit (0-4): ")

# Validasi input
if input_text.isdigit() and int(input_text) in penyakit:
    nama_penyakit = penyakit[int(input_text)]

    # Healthy prompt
    if nama_penyakit.lower() == "healthy":
        prompt = """
        Jelaskan tanda-tanda bahwa tanaman sawit dalam kondisi sehat. 
        Berikan informasi singkat mengenai ciri-ciri fisik dan pertumbuhan yang menunjukkan kesehatan optimal tanaman sawit.
        """
    else:
        # Disease prompt
        prompt = f"""
        Berikan informasi mengenai penyakit tanaman sawit: {nama_penyakit}.

        Tuliskan dalam format berikut:
        1. Deskripsi: (Satu paragraf singkat tentang apa itu penyakit ini)
        2. Efek: (Apa dampak negatifnya terhadap tanaman sawit)
        3. Rekomendasi: (Langkah penanganan atau pengobatan yang disarankan)

        Gunakan bahasa Indonesia yang formal dan padat.
        """

    # send query to the model
    response = client.chat(
        model=model, 
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0.2,
            #"num_predict": 300
        }
    )

    # Model response
    print("Respons model:")
    print(response["message"]["content"])

else:
    print("Input tidak valid. Silakan masukkan nomor antara 0 hingga 3.")