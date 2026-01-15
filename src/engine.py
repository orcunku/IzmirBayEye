import json
from datetime import datetime
import os

class AnalyticsEngine:
    """Predicts odor events using Eutrophication and Anaerobic Decay logic."""
    def __init__(self, db_path="history.json"):
        self.db_path = db_path

    def predict_risk(self, data):
        # 1. Biological Load (Algae + Turbidity)
        score = (data['chlorophyll'] * 30) + (data['turbidity'] * 0.5)
        
        # 2. Anaerobic Risk (The 'Smell' Factor)
        # Low Oxygen + Negative ORP = Immediate Odor
        if data['dissolved_oxygen'] < 3.5:
            score += 30
        if data['orp_value'] < 0:
            score += 20
            
        # 3. Chemical Pollution (Ammonia)
        score += (data['ammonia_levels'] * 10)
        
        # 4. Meteorology (Heat + Stagnation)
        if data['water_temp'] > 30: score += 10
        if data['wind_speed'] < 4: score += 15
            
        risk = round(min(score, 100), 1)
        self._save_to_history(risk, data)
        return risk

    def _save_to_history(self, risk, sensors):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "odor_risk": risk,
            "sensors": sensors
        }
        history = []
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                try: history = json.load(f)
                except: history = []
        history.append(entry)
        with open(self.db_path, "w") as f:
            json.dump(history[-100:], f, indent=4)
