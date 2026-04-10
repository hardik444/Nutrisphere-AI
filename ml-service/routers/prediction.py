from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    time = data.get("time", "night")

    if time == "night":
        return {
            "prediction": "High chance of junk food craving",
            "risk_score": 0.85,
            "suggestion": "Try fruits or nuts instead"
        }

    return {
        "prediction": "Healthy eating pattern",
        "risk_score": 0.2,
        "suggestion": "Keep it up!"
    }
