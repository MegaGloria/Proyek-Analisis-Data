# Bike Sharing Data Analysis & Dashboard

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan musim, kondisi cuaca, dan waktu dalam sehari. Hasil analisis divisualisasikan dalam dashboard interaktif menggunakan **Streamlit**.

## 📂 Struktur Direktori
```
submission/
│── dashboard/
│   ├── main_data.csv
│   ├── dashboard.py
│── data/
│   ├── day.csv
│   ├── hour.csv
│── notebook.ipynb
│── README.md
│── requirements.txt
│── url.txt
```

## 🛠 Instalasi dan Menjalankan Dashboard
1. **Pastikan Python sudah terinstal** (versi 3.7 ke atas direkomendasikan).
2. **Buat virtual environment (opsional, direkomendasikan)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Mac/Linux
   venv\Scripts\activate     # Untuk Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Jalankan dashboard Streamlit**
   ```bash
   streamlit run dashboard/dashboard.py
   ```
5. **Buka di browser**
   - Streamlit akan berjalan di `http://localhost:8501/`

## 📊 Analisis Data
- **Bagaimana pola penyewaan sepeda berdasarkan musim dan kondisi cuaca?**
  - Menampilkan rata-rata jumlah penyewaan berdasarkan musim dan kondisi cuaca.
  - Visualisasi: **Bar Chart**.
- **Kapan jam sibuk penyewaan sepeda dalam sehari?**
  - Menganalisis jam dengan jumlah penyewaan tertinggi.
  - Visualisasi: **Line Chart**.

## 🚀 Deployment
Untuk mengunggah ke **Streamlit Cloud**, lakukan langkah berikut:
1. Buat akun di [Streamlit Cloud](https://share.streamlit.io/).
2. Push kode ke **GitHub**.
3. Deploy melalui dashboard Streamlit dengan menghubungkan ke repository GitHub.
4. Tambahkan URL aplikasi ke dalam `url.txt`.

---
**Author: [Nama Anda]**
