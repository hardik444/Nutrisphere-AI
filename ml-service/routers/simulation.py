from fastapi import APIRouter

router = APIRouter()

@router.post("/simulate")
def simulate(data: dict):
    junk_freq = data.get("junk_food_per_week", 3)

    weight_gain = junk_freq * 0.2

    return {
        "future_30_days": {
            "weight_change": f"+{round(weight_gain,2)} kg",
            "energy_level": "Decreasing",
            "craving_increase": f"{junk_freq * 10}%"
        },
        "advice": "Reduce junk intake by 50% for better results"
    }
