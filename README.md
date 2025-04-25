# ☁︎🌤️ Analisis Kualitas Udara Kota Jakarta (AQI) Berdasarkan 5 Faktor Air Quality ☁︎🌤️

Sebuah mini-proyek berbasis **FastAPI** yang dapat memprediksi kualitas udara **kualitas udara**, berdasarkan input polutan udara.

## 📁 Struktur File

```
├── app.py                  # Endpoint API utama
├── knn_model.pkl           # File model Machine Learning yang telah dilatih
├── scaler.pkl              # File scaler untuk normalisasi fitur input
├── requirements.txt        # Daftar dependency yang dibutuhkan
```

## 🚀 Fitur API

- Prediksi kualitas udara
- Menerima input melalui metode POST
- Hasil prediksi: '1 untuk **Baik**', '2 untuk **Sedang**', '3 untuk **Tidak Sehat**', '4 untuk **Sangat Tidak Sehat**'

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/Daivageralda/titanic-fastapi.git
cd titanic-fastapi
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
fastapi dev
```

### 5. Akses Swagger UI

Buka browser ke:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "Name": "John Doe",
  "Pclass": 2,
  "Sex": "male",
  "Age": 30,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 13.5,
  "Embarked": "S"
}
```

## ✅ Contoh Output

```json
{
  "name": "John Doe",
  "prediction": 1,
  "result": "Survived"
}
```


> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
