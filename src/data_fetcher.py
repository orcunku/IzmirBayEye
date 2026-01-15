import random

class DataFetcher:
    def get_environmental_data(self):
        return {
            "wind_speed": random.uniform(2, 15),
            "water_temp": random.uniform(20, 35),
            "chlorophyll": random.uniform(0.1, 0.9)
        }
