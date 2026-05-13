from inference_sdk import InferenceHTTPClient
import ollama
import os

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="58c7Qs0Cbmt5M5MvbPXk"
)

image_path = "playground/original.jpg"

if os.path.exists(image_path):
    try:
        #input_image = input("Enter the path to your image: ")
        result = CLIENT.infer(image_path, model_id="palm-tree-leaves-diseases-old/2")
        
        nama_penyakit = result['predictions'][0]['class'].split('. ')[-1]
        print(nama_penyakit)
    
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Image file '{image_path}' does not exist.")

client = ollama.Client()
model = "gemma3:1b"
llm_input = nama_penyakit

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