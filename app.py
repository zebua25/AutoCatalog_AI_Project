import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="Auto Catalog AI", layout="centered")
st.title("📦 Auto-Catalog Generator dari Gambar + Deskripsi AI")

csv_path = os.path.join(os.path.dirname(__file__), "katalog_otomatis_final.csv")

if not os.path.exists(csv_path):
    st.error("❌ File katalog_otomatis_final.csv tidak ditemukan.")
    st.stop()

df = pd.read_csv(csv_path)

# Pastikan kolom yang dibutuhkan ada
required_cols = ['Nama File Gambar', 'Judul', 'Deskripsi', 'Harga']
for col in required_cols:
    if col not in df.columns:
        st.error(f"❌ Kolom '{col}' tidak ditemukan di CSV.")
        st.stop()

st.subheader("📋 Hasil Katalog Otomatis")

for idx, row in df.iterrows():
    col1, col2 = st.columns([1, 3])

    image_path = os.path.join(os.path.dirname(__file__), "images", row["Nama File Gambar"])
    
    if os.path.exists(image_path):
        image = Image.open(image_path)
        col1.image(image, caption=row["Judul"], use_column_width=True)
    else:
        col1.warning(f"🚫 Gambar tidak ditemukan: {row['Nama File Gambar']}")

    col2.markdown(f"### {row['Judul']}")
    col2.markdown(f"📝 {row['Deskripsi']}")
    col2.markdown(f"💰 Harga: **{row['Harga']}**")
    col2.markdown("---")

# Tombol download CSV hasil
st.download_button(
    label="📥 Download Katalog CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="katalog_otomatis_final.csv",
    mime="text/csv"
)
