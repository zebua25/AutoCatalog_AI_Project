import streamlit as st
import pandas as pd
import os
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Auto Catalog AI", layout="centered")
st.title("📦 Auto-Catalog Generator dari Gambar + Deskripsi AI")

# Path file CSV dan folder gambar relatif terhadap file app.py
csv_file = "katalog_otomatis_final.csv"
image_folder = "images"

# Validasi CSV
if not os.path.exists(csv_file):
    st.error(f"❌ File '{csv_file}' tidak ditemukan.")
    st.stop()

# Load data katalog
df = pd.read_csv(csv_file)

# Validasi kolom penting
required_cols = ['Nama File Gambar', 'Judul', 'Deskripsi', 'Harga']
for col in required_cols:
    if col not in df.columns:
        st.error(f"❌ Kolom '{col}' tidak ditemukan di CSV.")
        st.stop()

# Tampilkan katalog
st.subheader("🖼️ Katalog Otomatis dari AI")

for index, row in df.iterrows():
    col1, col2 = st.columns([1, 3])

    image_filename = row['Nama File Gambar']
    image_path = os.path.join(image_folder, image_filename)

    if os.path.exists(image_path):
        image = Image.open(image_path)
        col1.image(image, caption=row['Judul'], use_column_width=True)
    else:
        col1.warning(f"🚫 Gambar tidak ditemukan: {image_filename}")

    col2.markdown(f"### {row['Judul']}")
    col2.markdown(f"📝 {row['Deskripsi']}")
    col2.markdown(f"💰 **{row['Harga']}**")
    col2.markdown("---")

# Tombol download CSV
st.download_button(
    label="📥 Download Katalog CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="katalog_otomatis_final.csv",
    mime="text/csv"
)
