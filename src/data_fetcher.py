import random

class DataFetcher:
    """Handles data ingestion from sensors and satellite APIs."""
    
    def get_environmental_data(self):
        try:
            # In a real scenario, this would be a requests.get() call to an API
            data = {
                "wind_speed": round(random.uniform(2, 15), 2),  # km/h
                "water_temp": round(random.uniform(20, 35), 2), # Celsius
                "chlorophyll": round(random.uniform(0.1, 0.9), 3) # Index
            }
            return data
        except Exception as e:
            print(f"Error fetching sensor data: {e}")
            return None
