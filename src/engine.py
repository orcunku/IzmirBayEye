import json
from datetime import datetime
import os

class AnalyticsEngine:
    """The 'Brain' of BayEye AI. Calculates risk and persists data."""
    
    def __init__(self, db_path="history.json"):
        self.db_path = db_path

    def predict_risk(self, data):
        if not data:
            return 0.0

        # Weighted formula for H2S (Odor) Risk
        # Chlorophyll (Algae) is the main driver, Water Temp accelerates it.
        base_score = (data['chlorophyll'] * 65) + (data['water_temp'] * 1.1)
        
        # Stagnant water (Low wind) prevents gas dispersal
        if data['wind_speed'] < 5:
            base_score += 15
            
        risk = round(min(base_score, 100), 1)
        self._save_to_history(risk, data)
        return risk

    def _save_to_history(self, risk, sensors):
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "risk_level": risk,
            "sensor_snapshot": sensors
        }
        
        # Append to file logic
        history = []
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        
        history.append(log_entry)
        with open(self.db_path, "w") as f:
            json.dump(history[-100:], f, indent=4) # Keep last 100 entries
