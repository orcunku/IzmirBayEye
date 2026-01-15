from fastapi import FastAPI
from src.data_fetcher import DataFetcher
from src.engine import predict_odor_risk

app = FastAPI(title="BayEye AI - Monitoring System")
fetcher = DataFetcher()

@app.get("/predict")
async def get_prediction():
    w = fetcher.get_weather_data()
    s = fetcher.get_satellite_indices()
    risk = predict_odor_risk(w, s)
    
    return {
        "status": "Success",
        "odor_risk": f"{risk}%",
        "recommendation": "High Alert" if risk > 70 else "Normal"
    }
