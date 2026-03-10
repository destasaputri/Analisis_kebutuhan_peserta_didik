import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Analisis Kebutuhan Peserta Didik", layout="wide")

st.title("Dashboard Analisis Kebutuhan Peserta Didik")

df = pd.read_excel("Analisis Kebutuhan Peserta Didik.xlsx")

# =============================
# FUNGSI MEMBUAT DIAGRAM GARIS
# =============================
def line_chart(data, judul):

    mean_values = data.mean()

    fig, ax = plt.subplots()

    ax.plot(mean_values.index, mean_values.values, marker='o')

    for i,v in enumerate(mean_values.values):
        ax.text(i, v+0.02, round(v,2), ha='center')

    ax.set_title(judul)
    ax.set_ylabel("Rata-rata Skor")
    ax.grid(True)

    st.pyplot(fig)

# =============================
# GAYA BELAJAR
# =============================
st.header("1. Gaya Belajar Peserta Didik")

gaya_belajar = df.filter(regex="GB")

line_chart(gaya_belajar, "Kecenderungan Gaya Belajar")

# =============================
# MINAT DAN MOTIVASI
# =============================
st.header("2. Minat dan Motivasi Belajar")

minat = df.filter(regex="MMB")

line_chart(minat, "Kecenderungan Minat dan Motivasi")

# =============================
# KESULITAN BELAJAR
# =============================
st.header("3. Kesulitan dan Hambatan Belajar")

kesulitan = df.filter(regex="KHB")

line_chart(kesulitan, "Kecenderungan Kesulitan Belajar")

# =============================
# HARAPAN PESERTA DIDIK
# =============================
st.header("4. Harapan Peserta Didik")

harapan = df.filter(regex="HPD")

line_chart(harapan, "Kecenderungan Harapan Peserta Didik")
