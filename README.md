# ☁︎🌤️ Analisis Kualitas Udara Kota Jakarta (AQI) Berdasarkan 5 Faktor Air Quality ☁︎🌤️

Sebuah mini-proyek berbasis **FastAPI** yang dapat memprediksi kualitas udara **kualitas udara**, berdasarkan input polutan udara.

## 📁 Struktur File

```
├── app.py                  # File python yang berisi endpoint API utama
├── knn_model.pkl           # File model Machine Learning yang telah dilatih
├── scaler.pkl              # File scaler untuk normalisasi fitur input
├── requirements.txt        # Daftar dependency/library yang dibutuhkan
```

## 🚀 Fitur API

- Prediksi kualitas udara
- Menerima input melalui metode POST
- Hasil prediksi: '1 untuk **Baik**', '2 untuk **Sedang**', '3 untuk **Tidak Sehat**', '4 untuk **Sangat Tidak Sehat**'

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```cmd
git clone https://github.com/KhalilPradiptaLee/posttest_PDAB.git
cd posttest_PDAB
```

### 2. Buat Virtual Environment

```cmd
python -m venv .env
.env\Scripts\activate
```

### 3. Install Dependensi

```cmd
pip install -r requirements.txt
```

### 4. Jalankan API

```cmd
uvicorn app:app --reload
```

### 5. Akses Swagger UI

Buka browser ke:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "pm10": 51,
  "so2": 33,
  "co": 70,
  "o3": 66,
  "no2": 29
}
```

## ✅ Contoh Output

```json
{
  "prediction": 2,
  "kategori": "SEDANG"
}
```

> Dibuat sebagai bagian dari praktik tahap **Deployment** dengan menggunakan metode **CRISP-DM**.  
