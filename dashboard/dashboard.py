import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    day_df = pd.read_csv("data/day.csv")
    hour_df = pd.read_csv("data/hour.csv")
    
    # Preprocessing
    day_df["dteday"] = pd.to_datetime(day_df["dteday"])
    day_df["season"] = day_df["season"].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
    day_df["weathersit"] = day_df["weathersit"].map({1: "Clear", 2: "Cloudy", 3: "Light Rain/Snow", 4: "Heavy Rain/Snow"})
    
    return day_df, hour_df

day_df, hour_df = load_data()

# Dashboard Title
st.title("Bike Sharing Data Dashboard")

# Sidebar
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", day_df["season"].unique())
filtered_data = day_df[day_df["season"] == selected_season]

# Penyewaan Sepeda Berdasarkan Musim dan Cuaca
st.subheader("Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=filtered_data, x="weathersit", y="cnt", estimator=sum, ci=None, ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title(f"Total Penyewaan Sepeda di Musim {selected_season}")
st.pyplot(fig)

# Jam Sibuk Penyewaan Sepeda
st.subheader("Jam Sibuk Penyewaan Sepeda")
hourly_counts = hour_df.groupby("hr")["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(data=hourly_counts, x="hr", y="cnt", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pola Jam Sibuk Penyewaan Sepeda")
st.pyplot(fig)

# Clustering Hari Berdasarkan Penyewaan
st.subheader("Clustering Hari Berdasarkan Penyewaan")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(day_df['cnt'], bins=30, kde=True, ax=ax)
ax.set_xlabel("Jumlah Penyewaan")
ax.set_ylabel("Frekuensi")
ax.set_title("Distribusi Penyewaan Sepeda Harian")
st.pyplot(fig)

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Dibuat oleh Mega Gloria")
