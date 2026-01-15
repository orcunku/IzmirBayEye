import random

class DataFetcher:
    """Simulates real-time ingestion from biochemical bay sensors."""
    def get_environmental_data(self):
        return {
            "wind_speed": round(random.uniform(1, 15), 2),      # km/h
            "water_temp": round(random.uniform(18, 36), 2),      # Celsius
            "chlorophyll": round(random.uniform(0.1, 1.0), 3),   # Index
            "turbidity": round(random.uniform(5, 50), 2),        # NTU
            "dissolved_oxygen": round(random.uniform(1.5, 9.0), 2), # mg/L
            "ammonia_levels": round(random.uniform(0.01, 2.5), 3), # mg/L
            "orp_value": round(random.uniform(-200, 300), 0)      # mV (Redox)
        }
