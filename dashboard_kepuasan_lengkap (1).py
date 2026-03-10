# =====================================================
# GAYA BELAJAR
# =====================================================
st.header("1️⃣ Gaya Belajar Peserta Didik")

# Hitung rata-rata berdasarkan tipe gaya belajar
visual = df[["GB1","GB2","GB5"]].mean().mean()
auditori = df[["GB3","GB6"]].mean().mean()
kinestetik = df[["GB4","GB7"]].mean().mean()

kategori_gaya = ["Visual","Auditori","Kinestetik"]
nilai_gaya = [visual, auditori, kinestetik]

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(kategori_gaya, nilai_gaya, marker='o', linewidth=2)

# batas atas grafik
ax.set_ylim(0, max(nilai_gaya)+0.5)

# tampilkan nilai
for i,v in enumerate(nilai_gaya):
    ax.text(i, v+0.05, f"{v:.2f}", ha='center')

ax.set_title("Kecenderungan Gaya Belajar Peserta Didik")
ax.set_ylabel("Rata-rata Skor")
ax.set_xlabel("Tipe Gaya Belajar")

ax.grid(True)

ax.spines[['top','right']].set_visible(False)

plt.tight_layout()

st.pyplot(fig)
