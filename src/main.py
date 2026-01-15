from fastapi import FastAPI, HTTPException
from src.data_fetcher import DataFetcher
from src.engine import AnalyticsEngine
from src.notifications import NotificationService
import json

app = FastAPI(
    title="BayEye AI API",
    description="Backend for Izmir Bay Environmental Monitoring",
    version="1.1.0"
)

fetcher = DataFetcher()
engine = AnalyticsEngine()

@app.get("/predict")
async def get_current_status():
    data = fetcher.get_environmental_data()
    if not data:
        raise HTTPException(status_code=500, detail="Sensor Data Unavailable")
        
    risk = engine.predict_risk(data)
    push = NotificationService.notify_citizens(risk)
    
    return {
        "status": "Healthy" if risk < 70 else "Action Required",
        "risk_percentage": risk,
        "environment": data,
        "notification": push
    }

@app.get("/history")
async def get_logs():
    try:
        with open("history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
