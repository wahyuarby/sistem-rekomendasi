import streamlit as st
import pickle
import pandas as pd

# Load the recommendation model
@st.cache_resource
def load_model():
    with open("laptop_recommender.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# App setup
st.title("Sistem Rekomendasi Laptop")

# Load the model
model = load_model()

# User interaction
st.sidebar.header("Input Parameter")
user_input = st.sidebar.text_input("Masukkan spesifikasi/fitur laptop (misal: gaming, budget, ringan)")

if user_input:
    try:
        recommendations = model.recommend(user_input)  # Asumsikan model memiliki metode `recommend`
        st.write("Rekomendasi Laptop untuk Anda:")
        st.table(recommendations)  # Asumsikan hasil rekomendasi berupa DataFrame atau list
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses rekomendasi: {e}")
