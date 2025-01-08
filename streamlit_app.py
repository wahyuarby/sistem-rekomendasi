# Streamlit App untuk Laptop & Jurnal
st.title("Sistem Rekomendasi")
st.write("Wahyu Muhammad Arby 22.12.2553")
st.write("Amikatuzzain 22.12.2560")
st.write("ahcma Luhur 22.12.2577")

# Pilihan Sistem
choice = st.selectbox("Pilih Sistem Rekomendasi:", ["Laptop", "Jurnal"])

if choice == "Laptop":
    st.subheader("Sistem Rekomendasi Laptop")
    laptop_query = st.text_input("Masukkan nama laptop:")
    num_recommendations = st.slider("Jumlah rekomendasi", min_value=1, max_value=10, value=5)
    
    if st.button("Cari Laptop"):
        if laptop_query:
            with st.spinner("Mencari rekomendasi laptop..."):
                laptop_recommendations = recsys.recommend(laptop_query, topk=num_recommendations)
                if isinstance(laptop_recommendations, str):
                    st.write(laptop_recommendations)
                else:
                    st.write("Rekomendasi laptop untuk Anda:")
                    st.dataframe(laptop_recommendations)

elif choice == "Jurnal":
    st.subheader("Sistem Rekomendasi Jurnal")
    journal_query = st.text_input("Masukkan kata atau kalimat pencarian:")
    num_recommendations = st.slider("Jumlah rekomendasi jurnal", min_value=1, max_value=30, value=5)
    
    if st.button("Cari Jurnal"):
        if journal_query:
            with st.spinner("Mencari rekomendasi jurnal..."):
                journal_recommendations = recommendations(journal_query, top=num_recommendations)
                st.write("Rekomendasi jurnal untuk Anda:")
                if isinstance(journal_recommendations, list):
                    st.write(journal_recommendations[0])
                else:
                    for idx, row in journal_recommendations.iterrows():
                        st.write(f"{idx + 1}. {row['judul']}")
