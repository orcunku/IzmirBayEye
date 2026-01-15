from fastapi import FastAPI
from src.data_fetcher import DataFetcher
from src.engine import AnalyticsEngine
from src.notifications import NotificationService

app = FastAPI(title="BayEye AI Enterprise")
fetcher = DataFetcher()
engine = AnalyticsEngine()

@app.get("/status")
async def check_bay():
    data = fetcher.get_environmental_data()
    risk = engine.predict_risk(data)
    push = NotificationService.notify_citizens(risk)
    
    return {"risk_score": risk, "notification_sent": bool(push), "details": push}
