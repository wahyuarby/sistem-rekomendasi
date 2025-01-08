import streamlit as st
import pandas as pd
import pickle

# Load the model and dataset
@st.cache(allow_output_mutation=True)
def load_model_and_data():
    with open("laptop_recommender.pkl", "rb") as f:
        recommender = pickle.load(f)
    data = pd.read_csv('complete laptop data0.csv', encoding='ISO-8859-1')
    return recommender, data

recommender, data = load_model_and_data()

# Streamlit app
st.title("Sistem Rekomendasi Laptop")
st.write("Masukkan nama laptop untuk mendapatkan rekomendasi berdasarkan konten.")

# Input laptop name
input_laptop = st.text_input("Nama Laptop", "")

if st.button("Cari Rekomendasi"):
    if input_laptop:
        # Get recommendations
        recommendations = recommender.recommend(input_laptop)
        if isinstance(recommendations, str):
            st.error(recommendations)  # Display error if laptop not found
        else:
            st.write("Hasil Rekomendasi:")
            st.dataframe(recommendations)
            st.write("Grafik Harga Laptop yang Direkomendasikan:")
            st.bar_chart(data=recommendations.set_index("name")["Price"])
    else:
        st.warning("Masukkan nama laptop terlebih dahulu!")
