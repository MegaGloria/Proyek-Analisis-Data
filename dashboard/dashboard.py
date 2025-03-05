import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    day_df = pd.read_csv("data/day.csv")
    return day_df

day_df = load_data()

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

# Visualisasi Penyewaan Berdasarkan Jam
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=day_df.groupby("hr").mean().reset_index(), ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig)

# Insight
st.subheader("📌 Insight dari Data")
st.write(
    "1️⃣ Musim Fall memiliki jumlah penyewaan sepeda tertinggi dibanding musim lainnya.\n"
    "2️⃣ Penyewaan sepeda meningkat tajam pada jam commuting (07:00-09:00 dan 17:00-19:00).\n"
    "3️⃣ Tren ini menunjukkan bahwa sepeda digunakan sebagai alat transportasi sehari-hari."
)

# Footer
st.markdown("---")
st.markdown("**Dashboard ini dikembangkan oleh Mega Gloria**")
