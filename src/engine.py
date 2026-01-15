import json
from datetime import datetime

class AnalyticsEngine:
    def predict_risk(self, data):
        # AI Logic: Temperature and Algae (Chlorophyll) are key drivers
        score = (data['chlorophyll'] * 60) + (data['water_temp'] * 1.2)
        if data['wind_speed'] < 5: score += 15
        risk = round(min(score, 100), 1)
        
        # Log to History (Persistence)
        log = {"time": datetime.now().isoformat(), "risk": risk}
        with open("history.json", "a") as f:
            f.write(json.dumps(log) + "\n")
        return risk
