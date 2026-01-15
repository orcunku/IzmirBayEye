from fastapi import FastAPI
from src.data_fetcher import DataFetcher
from src.engine import AnalyticsEngine
from src.notifications import NotificationService

app = FastAPI(title="BayEye AI Enterprise")
fetcher = DataFetcher()
engine = AnalyticsEngine()

@app.get("/monitor")
async def monitor_bay():
    data = fetcher.get_environmental_data()
    risk = engine.predict_risk(data)
    alert = NotificationService.get_alert(risk)
    return {"risk": f"{risk}%", "sensors": data, "alert": alert}
