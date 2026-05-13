import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="SawitAI - Diagnosa Penyakit Tanaman Sawit",
    layout="centered"
)

# Helper function  
def fetch_diseases():
    try:
        response = requests.get(f"{BASE_URL}/diseases")
        response.raise_for_status()
        return response.json().get("diseases", {})
    except requests.exceptions.RequestException as e:
        return {"Error fetching diseases": {str(e)}}

def get_disease_info(id: int):
    try:
        response = requests.get(f"{BASE_URL}/disease/{selected_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"Error fetching disease info": {str(e)}}
    

st.title("SawitAI - Diagnosa Penyakit Tanaman Sawit")
diseases = fetch_diseases()

if diseases:
    disease_option = {v: k for k, v in diseases.items()}

    # Dropdown selection
    selected_disease = st.selectbox(
        "Pilih kondisi tanaman sawit:",
        options=list(disease_option.keys())
    )

    selected_id = disease_option[selected_disease]

    # LLM Response Button
    if st.button("Dapatkan Informasi Penyakit"):
        with st.spinner("Loading..."):
            disease_info = get_disease_info(selected_id)

            if "error" in disease_info:
                st.error(disease_info["LLM error"])
            else:
                st.divider()
                st.subheader(f"Informasi tentang {selected_disease}: \n {disease_info.get('information')}")

else:
    st.error("Gagal memuat daftar penyakit. Silakan coba lagi nanti.")