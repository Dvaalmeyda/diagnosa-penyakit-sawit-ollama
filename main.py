import ollama
from config import Config

class SawitAI:
    def __init__(self):
        self.client = ollama.Client()
        self.penyakit_list = {
            0: "Healthy", 
            1: "Black Scorch", 
            2: "Fusarium Wilt", 
            3: "Leaf Spots",
            4: "Magnesium Deficiency",
            5: "Manganese Deficiency",
            6: "Parlatoria Blanchardi",
            7: "Potassium Deficiency",
            8: "Rachis Blight",
        }

    def get_penyakit_info(self, index: int):
        # Validasi
        if index not in self.penyakit_list:
            return "Penyakit tidak ditemukan."

        nama_penyakit = self.penyakit_list[index]
        
        # Prompt
        if nama_penyakit.lower() == "healthy":
            prompt = Config.SYSTEM_PROMPT_HEALTHY
        else:
            prompt = Config.PROMPT_TEMPLATE_DISEASE.format(nama_penyakit=nama_penyakit)

        try:
            # Request ke Model
            response = self.client.chat(
                model=Config.MODEL,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": Config.TEMPERATURE}
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Error menghubungi model: {str(e)}"

# Execution
if __name__ == "__main__":
    app = SawitAI()
    
    print("Daftar Penyakit Tanaman Sawit:")
    for k, v in app.penyakit_list.items():
        print(f"{k}: {v}")

    pilihan = input("\nPilih nomor penyakit (0-8): ")
    
    if pilihan.isdigit():
        hasil = app.get_penyakit_info(int(pilihan))
        print("\nRespons Model:\n", hasil)
    else:
        print("Input harus berupa angka yang tertera (0-8).")