import random

class DataFetcher:
    """Simulates fetching real-time environmental data for Izmir Bay."""
    def get_weather_data(self):
        return {
            "wind_speed": random.uniform(2, 12), 
            "air_temp": random.uniform(22, 35)
        }

    def get_satellite_indices(self):
        return {
            "chlorophyll_index": random.uniform(0.1, 0.9),
            "turbidity": random.uniform(10, 80)
        }
