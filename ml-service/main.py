from fastapi import FastAPI
from routers import prediction, simulation

app = FastAPI()

app.include_router(prediction.router)
app.include_router(simulation.router)

@app.get("/")
def home():
    return {"message": "ML Service Running 🚀"}
