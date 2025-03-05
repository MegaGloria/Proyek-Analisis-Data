import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "../data/day.csv")
    day_df = pd.read_csv(file_path)
    return day_df

day_df = load_data()

# Mapping Season Names
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season"] = day_df["season"].map(season_map)

# Dashboard Title
st.title("📊 Dashboard Penyewaan Sepeda")

# Sidebar Filters
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", ['All'] + list(day_df['season'].unique()))

if season_filter != 'All':
    day_df = day_df[day_df['season'] == season_filter]

# Visualisasi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x="season", y="cnt", data=day_df, ci=None, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig)

# Menampilkan Statistik Dasar
st.subheader("📈 Statistik Data Penyewaan Sepeda")
st.write(day_df.describe())
