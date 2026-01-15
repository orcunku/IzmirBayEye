from fastapi import FastAPI, UploadFile, File
from .engine import calculate_environmental_metrics, get_ai_forecast, rag_expert_chat

app = FastAPI(title="Izmir BayEye AI - Pro 2026 Edition")

@app.get("/monitor")
async def monitor_endpoint():
    report, agent_decision = calculate_environmental_metrics()
    forecast = get_ai_forecast()
    
    return {
        "telemetry": report,
        "ai_forecast": {"next_risk": forecast},
        "agent_status": {"current_action": agent_decision}
    }

@app.post("/verify-visual")
async def verify_visual(file: UploadFile = File(...)):
    """MULTIMODAL AI LAYER: Simulates Computer Vision verification."""
    # In a real 2026 app, you'd run a YOLO model here.
    return {
        "filename": file.filename,
        "vision_analysis": "Detected potential Algal Bloom in top-right quadrant.",
        "confidence": "89%"
    }

@app.get("/ask-expert")
async def ask_ai(query: str):
    """GENERATIVE RAG LAYER: Interactive chatbot."""
    response = rag_expert_chat(query)
    return {"query": query, "expert_response": response}
