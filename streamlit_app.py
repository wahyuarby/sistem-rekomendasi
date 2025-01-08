import streamlit as st
import pickle
import pandas as pd

# Fungsi untuk memuat model
@st.cache_resource
def load_model():
    try:
        with open("laptop_recommender.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("File model 'laptop_recommender.pkl' tidak ditemukan. Pastikan file tersebut ada di direktori.")
    except pickle.UnpicklingError:
        st.error("Terjadi kesalahan saat memuat file model. Pastikan file model kompatibel.")

# Konfigurasi aplikasi
st.title("Sistem Rekomendasi Laptop")

# Muat model
model = load_model()

# Input dari pengguna
st.sidebar.header("Input Parameter")
user_input = st.sidebar.text_input("Masukkan spesifikasi/fitur laptop (misal: gaming, budget, ringan)")

if user_input and model:
    try:
        # Asumsikan model memiliki metode `recommend` yang mengembalikan DataFrame atau list
        recommendations = model.recommend(user_input)
        st.write("Rekomendasi Laptop untuk Anda:")
        st.table(recommendations)
    except AttributeError:
        st.error("Model tidak memiliki metode 'recommend'. Periksa implementasi model Anda.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses rekomendasi: {e}")
