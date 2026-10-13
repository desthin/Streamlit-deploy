import streamlit as st
from google import genai

# Konfigurasi halaman
st.set_page_config(
    page_title="Chatbot IT Rumah Sakit",
    page_icon="🏥",
    layout="wide"
)

# --- SIDEBAR (PENGATURAN) ---
with st.sidebar:
    st.subheader("Pengaturan")
    
    # Pilihan Model
    model_choice = st.selectbox(
        "Model",
        ["gemini-2.5-flash", "gemini-1.5-pro"]
    )
    
    # Pengaturan Temperature
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.20,
        step=0.01
    )
    
    st.markdown("Tekan Reset untuk menghapus riwayat percakapan.")
    
    # Tombol Reset
    if st.button("Reset"):
        st.session_state.messages = []
        st.rerun()

# --- HALAMAN UTAMA ---
st.title("Chatbot IT Rumah Sakit")
st.caption("Asisten Pintar Layanan & Analitik IT Rumah Sakit")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan pesan chat sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dari pengguna
if prompt := st.chat_input("Tulis pertanyaan seputar IT Rumah Sakit di sini..."):
    # Simpan dan tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respon dari Asisten
    with st.chat_message("assistant"):
        with st.spinner("Menganalisis..."):
            # Contoh respon sederhana (bisa diintegrasikan dengan Gemini API sesuai kebutuhan)
            response_text = f"Baik, saya akan membantu menganalisis terkait kendala IT Rumah Sakit mengenai: '{prompt}'."
            st.markdown(response_text)
            
            # Simpan respon asisten
            st.session_state.messages.append({"role": "assistant", "content": response_text})
