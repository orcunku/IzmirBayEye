import random

class DataFetcher:
    """Simulates a multi-sensor array for Water Quality & Meteorology."""
    def get_environmental_data(self):
        return {
            # Physical parameters
            "wind_speed": round(random.uniform(1, 15), 2),
            "water_temp": round(random.uniform(18, 36), 2),
            # Biological indicators
            "chlorophyll": round(random.uniform(0.1, 1.0), 3),
            "turbidity": round(random.uniform(5, 50), 2), # NTU units
            # Chemical indicators
            "dissolved_oxygen": round(random.uniform(1.5, 9.0), 2), # mg/L
            "ammonia_levels": round(random.uniform(0.01, 2.5), 3), # mg/L
            "orp_value": round(random.uniform(-200, 300), 0)      # mV (Redox)
        }
