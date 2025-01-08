import streamlit as st
import pickle
import pandas as pd

# Fungsi untuk memuat file pickle
def load_data(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

# Judul aplikasi
st.title("Laptop Recommender System")

# Memuat file laptop_recommender.pkl
file_path = 'laptop_recommender.pkl'  # Ganti jalur jika file berada di lokasi berbeda
try:
    recommender_data = load_data(file_path)
    st.success("File berhasil dimuat!")

    # Jika data berupa DataFrame, tampilkan
    if isinstance(recommender_data, pd.DataFrame):
        st.write("### Dataframe Preview")
        st.dataframe(recommender_data)
    else:
        # Tampilkan tipe data lain
        st.write("### Data Content")
        st.write(recommender_data)

    # Contoh interaksi pengguna (sesuaikan dengan use case)
    st.write("### Rekomendasi Laptop")
    user_input = st.text_input("Masukkan kriteria laptop (contoh: budget, RAM, dll.):")
    if user_input:
        st.write(f"Rekomendasi berdasarkan input: {user_input}")
        # Placeholder logika rekomendasi (sesuaikan dengan data Anda)
        st.write("[Hasil rekomendasi akan ditampilkan di sini]")

except FileNotFoundError:
    st.error(f"File tidak ditemukan di lokasi: {file_path}")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
