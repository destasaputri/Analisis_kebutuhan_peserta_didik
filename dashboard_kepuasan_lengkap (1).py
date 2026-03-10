import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Analisis Kebutuhan Peserta Didik", layout="wide")

st.title("Dashboard Analisis Kebutuhan Belajar Peserta Didik")

# Load data
df = pd.read_excel("Analisis Kebutuhan Peserta Didik.xlsx")

# Kelompok indikator sesuai angket
gaya_belajar = df.filter(regex="GB")
minat_motivasi = df.filter(regex="MMB")
kesulitan = df.filter(regex="KHB")
harapan = df.filter(regex="HPD")

# Hitung rata-rata
mean_gb = gaya_belajar.mean().mean()
mean_mmb = minat_motivasi.mean().mean()
mean_khb = kesulitan.mean().mean()
mean_hpd = harapan.mean().mean()

kategori = [
"Gaya Belajar",
"Minat & Motivasi",
"Kesulitan Belajar",
"Harapan Peserta Didik"
]

nilai = [
mean_gb,
mean_mmb,
mean_khb,
mean_hpd
]

# Diagram garis
st.subheader("Kecenderungan Kebutuhan Belajar Peserta Didik")

fig, ax = plt.subplots()

ax.plot(kategori, nilai, marker='o', linewidth=2)

for i,v in enumerate(nilai):
    ax.text(i, v+0.02, round(v,2), ha='center')

ax.set_ylabel("Rata-rata Skor")
ax.set_title("Diagram Kecenderungan Kebutuhan Peserta Didik")
ax.grid(True)

st.pyplot(fig)
