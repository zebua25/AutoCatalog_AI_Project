import streamlit as st
import pandas as pd
from PIL import Image
import os

# Path lokal atau gdrive
csv_path = "katalog_otomatis_final.csv"
img_folder = "/content/drive/MyDrive/AutoCatalog_AI_Project/dataset/"

# Load data
df = pd.read_csv(csv_path)

# UI
st.title("🛍️ Auto-Catalog E-Commerce by AI")
st.markdown("Sistem cerdas untuk membuat katalog produk otomatis dari gambar dan AI 🚀")

# Tampilkan semua produk
for index, row in df.iterrows():
    col1, col2 = st.columns([1, 2])

    with col1:
        img_path = os.path.join(img_folder, row["Nama File Gambar"])
        image = Image.open(img_path)
        st.image(image, caption=row["Judul"], use_column_width=True)

    with col2:
        st.subheader(row["Judul"])
        st.markdown(f"**Kategori:** {row['Kategori']}")
        st.markdown(f"**Harga:** {row['Harga']}")
        st.markdown(row["Deskripsi"])
        st.markdown("---")
