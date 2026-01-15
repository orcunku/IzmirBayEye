def predict_odor_risk(weather, satellite):
    """Scientific logic to predict odor based on stagnant water and algae."""
    # Chlorophyll contributes 60%, Temp contributes 40%
    base_score = (satellite['chlorophyll_index'] * 60) + (weather['air_temp'] * 1.1)
    
    # Penalty for low wind speed (odor accumulation)
    if weather['wind_speed'] < 5:
        base_score += 15
        
    return round(min(base_score, 100), 1)
