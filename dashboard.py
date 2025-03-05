
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Convert date column to datetime format
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Mapping categorical values
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_mapping = {1: "Clear", 2: "Cloudy", 3: "Light Rain/Snow", 4: "Heavy Rain/Snow"}

day_df["season"] = day_df["season"].map(season_mapping)
day_df["weathersit"] = day_df["weathersit"].map(weather_mapping)

# Title
st.title("Bike Sharing Data Dashboard")

# Sidebar filters
selected_season = st.sidebar.selectbox("Pilih Musim", day_df["season"].unique())

# Filter data based on selection
filtered_data = day_df[day_df["season"] == selected_season]

# Visualisasi 1: Penyewaan sepeda berdasarkan cuaca
st.subheader("Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
weather_trend = filtered_data.groupby("weathersit")["cnt"].mean()
fig, ax = plt.subplots()
weather_trend.plot(kind="bar", ax=ax, color=["blue", "gray", "orange", "red"], alpha=0.7)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
ax.set_title("Penyewaan Sepeda per Kondisi Cuaca")
st.pyplot(fig)

# Visualisasi 2: Pola Penyewaan Sepeda per Jam
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam")
hourly_trend = hour_df.groupby("hr")["cnt"].mean()
fig2, ax2 = plt.subplots()
ax2.plot(hourly_trend.index, hourly_trend.values, marker="o", linestyle="-", color="b", alpha=0.8)
ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Jumlah Penyewaan")
ax2.set_title("Pola Penyewaan Sepeda dalam Sehari")
ax2.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig2)
