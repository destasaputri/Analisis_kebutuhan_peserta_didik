import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="Dashboard Analisis Kebutuhan Peserta Didik",
    layout="wide"
)

st.title("📊 Dashboard Analisis Kebutuhan Peserta Didik")
st.write("Visualisasi hasil angket kebutuhan belajar siswa")

# =====================================================
# LOAD DATA
# =====================================================
df = pd.read_excel("Analisis Kebutuhan Peserta Didik.xlsx")

# =====================================================
# GRAFIK GAYA BELAJAR
# =====================================================
st.header("1️⃣ Gaya Belajar Peserta Didik")

visual = df[["GB1","GB2","GB5"]].mean().mean()
auditori = df[["GB3","GB6"]].mean().mean()
kinestetik = df[["GB4","GB7"]].mean().mean()

kategori_gaya = ["Visual","Auditori","Kinestetik"]
nilai_gaya = [visual, auditori, kinestetik]

fig1, ax1 = plt.subplots(figsize=(8,5))

ax1.plot(kategori_gaya, nilai_gaya, marker='o', linewidth=2)

ax1.set_ylim(0, max(nilai_gaya)+0.5)

for i,v in enumerate(nilai_gaya):
    ax1.text(i, v+0.05, f"{v:.2f}", ha='center')

ax1.set_title("Kecenderungan Gaya Belajar")
ax1.set_ylabel("Rata-rata Skor")
ax1.set_xlabel("Tipe Gaya Belajar")

ax1.grid(True)
ax1.spines[['top','right']].set_visible(False)

plt.tight_layout()

st.pyplot(fig1)

# =====================================================
# FUNGSI GRAFIK
# =====================================================
def line_chart(data, judul):

    mean_values = data.mean()

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(mean_values.index, mean_values.values,
            marker='o', linewidth=2)

    ax.set_ylim(0, mean_values.max()+0.5)

    for i,v in enumerate(mean_values.values):
        ax.text(i, v+0.05, f"{v:.2f}", ha='center')

    ax.set_title(judul)
    ax.set_ylabel("Rata-rata Skor")
    ax.set_xlabel("Indikator")

    ax.grid(True)
    ax.spines[['top','right']].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)

# =====================================================
# MINAT DAN MOTIVASI
# =====================================================
st.header("2️⃣ Minat dan Motivasi Belajar")

minat = df.filter(regex="MMB")

line_chart(minat, "Kecenderungan Minat dan Motivasi")

# =====================================================
# KESULITAN BELAJAR
# =====================================================
st.header("3️⃣ Kesulitan dan Hambatan Belajar")

kesulitan = df.filter(regex="KHB")

line_chart(kesulitan, "Kecenderungan Kesulitan Belajar")

# =====================================================
# HARAPAN PESERTA DIDIK
# =====================================================
st.header("4️⃣ Harapan Peserta Didik")

harapan = df.filter(regex="HPD")

line_chart(harapan, "Kecenderungan Harapan Peserta Didik")

# =====================================================
# TAMPILKAN DATA
# =====================================================
st.header("📄 Data Hasil Angket")

st.dataframe(df)
