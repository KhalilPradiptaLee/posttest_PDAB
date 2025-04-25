from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Inisialisasi FastAPI
app = FastAPI(title="Air Quality Prediction API")

# Load model dan scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("knn_model.pkl", "rb") as f:

    model = pickle.load(f)

# Mapping kategori
kategori_mapping = {
    1: "BAIK",
    2: "SEDANG",
    3: "TIDAK SEHAT",
    4: "SANGAT TIDAK SEHAT",
    5: "BERBAHAYA",
}

# Input schema
class Pollution(BaseModel):
    pm10: float
    so2: float
    co: float
    o3: float
    no2: float

@app.get("/")
def read_root():
    return {"message": "Air Quality Prediction API is running"}

@app.post("/predict")
def predict_air_quality(data: Pollution):
    # Ubah data ke DataFrame
    df = pd.DataFrame([{
        "pm10": data.pm10,
        "so2": data.so2,
        "co": data.co,
        "o3": data.o3,
        "no2": data.no2
    }])

    # Normalisasi
    df_scaled = scaler.transform(df)

    # Prediksi
    prediction = model.predict(df_scaled)[0]

    # Mapping hasil prediksi ke kategori
    kategori = kategori_mapping.get(int(prediction), "Unknown")

    return {
        "prediction": int(prediction),
        "kategori": kategori
    }
