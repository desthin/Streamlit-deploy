import streamlit as st

st.title("Streamlit Chatbot App")
st.write("Halo! Ini adalah aplikasi Streamlit pertama saya.")

user_input = st.chat_input("Tulis pesan Anda di sini...")
if user_input:
    st.write(f"Anda berkata: {user_input}")
