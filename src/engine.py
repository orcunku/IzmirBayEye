import json
from datetime import datetime
import os

class AnalyticsEngine:
    """Advanced biochemical logic for H2S (Odor) prediction."""
    def __init__(self, db_path="history.json"):
        self.db_path = db_path

    def predict_risk(self, data):
        # 1. Biological Load (30% weight)
        score = (data['chlorophyll'] * 30) + (data['turbidity'] * 0.5)
        
        # 2. Anaerobic/Odor Factor (50% weight)
        if data['dissolved_oxygen'] < 3.5: score += 30 # Hypoxia penalty
        if data['orp_value'] < 0: score += 20          # Reducing environment penalty
            
        # 3. Chemical/Meteo Stress (20% weight)
        score += (data['ammonia_levels'] * 10)
        if data['water_temp'] > 30: score += 5
        if data['wind_speed'] < 4: score += 15 # Stagnation penalty
            
        risk = round(min(score, 100), 1)
        self._save_to_history(risk, data)
        return risk

    def _save_to_history(self, risk, sensors):
        entry = {"timestamp": datetime.now().isoformat(), "risk": risk, "sensors": sensors}
        history = []
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                try: history = json.load(f)
                except: history = []
        history.append(entry)
        with open(self.db_path, "w") as f:
            json.dump(history[-100:], f, indent=4) # Store last 100 snapshots
