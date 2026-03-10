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
# FUNGSI MEMBUAT DIAGRAM GARIS
# =====================================================
def line_chart(data, judul):

    mean_values = data.mean()

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(mean_values.index, mean_values.values,
            marker='o', linewidth=2)

    # batas atas grafik supaya label tidak keluar
    ax.set_ylim(0, mean_values.max() + 0.5)

    # menampilkan angka di titik
    for i, v in enumerate(mean_values.values):
        ax.text(i, v + 0.05, f"{v:.2f}", ha='center')

    ax.set_title(judul)
    ax.set_ylabel("Rata-rata Skor")
    ax.set_xlabel("Indikator")

    ax.grid(True)

    # membuat grafik lebih clean
    ax.spines[['top','right']].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)

# =====================================================
# GAYA BELAJAR
# =====================================================
st.header("1️⃣ Gaya Belajar Peserta Didik")

gaya_belajar = df.filter(regex="GB")

line_chart(gaya_belajar, "Kecenderungan Gaya Belajar")

# =====================================================
# MINAT DAN MOTIVASI BELAJAR
# =====================================================
st.header("2️⃣ Minat dan Motivasi Belajar")

minat_motivasi = df.filter(regex="MMB")

line_chart(minat_motivasi, "Kecenderungan Minat dan Motivasi")

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
