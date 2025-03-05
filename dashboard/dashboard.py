import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset with error handling
def load_data():
    try:
        file_path = os.path.abspath("data/day.csv")
        if not os.path.exists(file_path):
            st.error(f"File tidak ditemukan: {file_path}")
            return None
        day_df = pd.read_csv(file_path)
        return day_df
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        return None

day_df = load_data()
if day_df is None:
    st.stop()

# Mapping Season Names
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season"] = day_df["season"].map(season_map)

# Convert date column
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Dashboard Title
st.title("📊 Dashboard Analisis Penyewaan Sepeda")

# Sidebar Filters
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", ['All'] + list(day_df['season'].unique()))
if season_filter != 'All':
    day_df = day_df[day_df['season'] == season_filter]

# 1️⃣ Tren Penyewaan Sepeda
st.subheader("📈 Tren Penyewaan Sepeda Sepanjang Waktu")
fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(x=day_df['dteday'], y=day_df['cnt'], ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda Harian")
st.pyplot(fig)

# 2️⃣ Pengaruh Cuaca terhadap Penyewaan
st.subheader("🌤️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(x=day_df['weathersit'], y=day_df['cnt'], ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# 3️⃣ Distribusi Penyewaan Berdasarkan Musim
st.subheader("🌿🚴 Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=day_df['season'], y=day_df['cnt'], ci=None, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
ax.set_title("Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Menampilkan Statistik Dasar
st.subheader("📊 Statistik Data Penyewaan Sepeda")
st.write(day_df.describe())
