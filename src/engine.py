import json
import datetime
import random
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

DB_PATH = "history.json"

def calculate_environmental_metrics():
    """Generates sensor data and executes Agentic Decisions."""
    oxygen = round(random.uniform(2.0, 9.0), 2)
    orp = round(random.uniform(-150, 350), 2)
    temp = round(random.uniform(18, 28), 2)

    risk_score = 30 + (7 - oxygen) * 8 + (temp - 20) * 2
    if orp < 0: risk_score += 15
    risk_score = min(max(round(risk_score, 2), 0), 100)

    data_point = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "oxygen": oxygen, "orp": orp, "temperature": temp,
        "risk_score": risk_score
    }
    
    _save_to_history(data_point)
    
    # --- AGENTIC AI LAYER ---
    # The 'Guard' makes an autonomous decision based on risk
    agent_action = "Monitoring"
    if risk_score > 75:
        agent_action = "CRITICAL_ALERT: Drafting report to Municipality."
    elif risk_score > 50:
        agent_action = "CAUTION: Flagging for manual verification."

    return data_point, agent_action

def _save_to_history(data):
    try:
        with open(DB_PATH, "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    history.append(data)
    with open(DB_PATH, "w") as f:
        json.dump(history[-100:], f, indent=4)

def get_ai_forecast():
    """Predictive ML Layer."""
    try:
        with open(DB_PATH, "r") as f:
            history = json.load(f)
        if len(history) < 5: return "Collecting data..."
        
        df = pd.DataFrame(history)
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df['risk_score'].values
        model = LinearRegression().fit(X, y)
        prediction = model.predict([[len(df)]])[0]
        return round(float(prediction), 2)
    except:
        return "N/A"

def rag_expert_chat(query: str):
    """RAG-lite Layer: Simulates a chatbot answering based on local knowledge."""
    knowledge = {
        "odor": "Izmir Bay odors are typically caused by low dissolved oxygen and anaerobic activity.",
        "solution": "Increasing circulation and dredging the inner bay are common solutions.",
        "safe_limit": "A risk score below 40 is considered safe for the Izmir coastline."
    }
    for key in knowledge:
        if key in query.lower():
            return knowledge[key]
    return "I am currently analyzing the Bay data to answer that more accurately."
