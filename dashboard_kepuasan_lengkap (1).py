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
# FUNGSI MEMBUAT GRAFIK
# =====================================================
def grafik_garis(label, nilai, judul, xlabel):

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(label, nilai, marker='o', linewidth=2)

    ax.set_ylim(0, max(nilai)+0.5)

    for i,v in enumerate(nilai):
        ax.text(i, v+0.05, f"{v:.2f}", ha='center')

    ax.set_title(judul)
    ax.set_ylabel("Rata-rata Skor")
    ax.set_xlabel(xlabel)

    ax.grid(True)
    ax.spines[['top','right']].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)

# =====================================================
# 1 GAYA BELAJAR
# =====================================================
st.header("1️⃣ Gaya Belajar Peserta Didik")

visual = df[["GB1","GB2","GB5"]].mean().mean()
auditori = df[["GB3","GB6"]].mean().mean()
kinestetik = df[["GB4","GB7"]].mean().mean()

label_gaya = ["Visual","Auditori","Kinestetik"]
nilai_gaya = [visual, auditori, kinestetik]

grafik_garis(
    label_gaya,
    nilai_gaya,
    "Kecenderungan Gaya Belajar Peserta Didik",
    "Tipe Gaya Belajar"
)

# =====================================================
# 2 MINAT DAN MOTIVASI BELAJAR
# =====================================================
st.header("2️⃣ Minat dan Motivasi Belajar")

motivasi_ekstrinsik = df[["MMB1"]].mean().mean()
minat = df[["MMB2"]].mean().mean()
motivasi_intrinsik = df[["MMB3","MMB4","MMB5"]].mean().mean()

label_motivasi = [
    "Minat",
    "Motivasi Intrinsik",
    "Motivasi Ekstrinsik"
]

nilai_motivasi = [
    minat,
    motivasi_intrinsik,
    motivasi_ekstrinsik
]

grafik_garis(
    label_motivasi,
    nilai_motivasi,
    "Kecenderungan Minat dan Motivasi Belajar",
    "Aspek Motivasi"
)

# =====================================================
# 3 KESULITAN BELAJAR
# =====================================================
st.header("3️⃣ Kesulitan dan Hambatan Belajar")

kesulitan = df.filter(regex="KHB").mean()

grafik_garis(
    kesulitan.index.tolist(),
    kesulitan.values.tolist(),
    "Kecenderungan Kesulitan Belajar",
    "Indikator Kesulitan"
)

# =====================================================
# 4 HARAPAN PESERTA DIDIK
# =====================================================
st.header("4️⃣ Harapan Peserta Didik")

harapan = df.filter(regex="HPD").mean()

grafik_garis(
    harapan.index.tolist(),
    harapan.values.tolist(),
    "Kecenderungan Harapan Peserta Didik",
    "Indikator Harapan"
)

# =====================================================
# TAMPILKAN DATA
# =====================================================
st.header("📄 Data Hasil Angket")

st.dataframe(df)
