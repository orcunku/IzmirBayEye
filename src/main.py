from fastapi import FastAPI
from src.data_fetcher import DataFetcher
from src.engine import AnalyticsEngine
from src.notifications import NotificationService

app = FastAPI(title="BayEye AI: Izmir Bay Smart Monitor")
fetcher = DataFetcher()
engine = AnalyticsEngine()

@app.get("/monitor/current")
async def get_status():
    data = fetcher.get_environmental_data()
    risk = engine.predict_risk(data)
    alert = NotificationService.get_alert(risk)
    
    return {
        "odor_risk_score": f"{risk}%",
        "parameters": data,
        "notification": alert
    }
