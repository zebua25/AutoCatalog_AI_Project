import streamlit as st
import pandas as pd
import os

# Judul Aplikasi
st.set_page_config(page_title="Auto Catalog AI", layout="centered")
st.title("📦 Auto-Catalog Generator dari Gambar + Deskripsi AI")

# Path dinamis untuk file CSV
csv_path = os.path.join(os.path.dirname(__file__), "katalog_otomatis_final.csv")

# Validasi keberadaan file CSV
if not os.path.exists(csv_path):
    st.error("❌ File 'katalog_otomatis_final.csv' tidak ditemukan.")
    st.info("🔁 Pastikan file CSV sudah diunggah ke folder yang sama dengan app.py di GitHub.")
    st.stop()

# Load data CSV
df = pd.read_csv(csv_path)

# Tampilkan preview data
st.subheader("📋 Hasil Katalog Otomatis")
st.dataframe(df, use_container_width=True)

# Tampilkan info ringkas
st.markdown(f"✅ Jumlah Produk: **{len(df)}**")
st.success("Katalog berhasil dimuat dan ditampilkan! 🎉")

# Optional: Simpan ulang file jika user ingin download
st.download_button(
    label="📥 Download Katalog CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="katalog_otomatis_final.csv",
    mime="text/csv"
)
