# NutriSphere AI 🧠🥗

> Predictive Behavioral Nutrition System — We don't count calories. We predict decisions.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](docker-compose.yml)
[![Cloud Run](https://img.shields.io/badge/GCP-Cloud_Run-orange)](infrastructure/)

---

## Problem

73% of users abandon nutrition apps within 2 weeks. Why?
Because they all react — they record what happened after the fact.
Unhealthy eating decisions are predictable and preventable within a 40–120 second window.
No app intercepts that window.

## Solution

NutriSphere AI is a predictive system that:
- **Predicts** your next meal decision using behavioral + contextual signals
- **Intervenes** before unhealthy choices — not after
- **Simulates** the 7/30-day consequence of your current trajectory
- **Evolves** a Digital Nutrition Twin that learns your unique patterns

## Features

| Feature | Description |
|---|---|
| 🔮 Predictive Eating Engine | LSTM model predicts next food choice with confidence scoring |
| 🚨 Smart Interventions | Pre-emptive notifications within the decision window |
| 🔄 Habit Loop Analyzer | Detects cue → routine → reward cycles |
| 🌍 Context-Aware AI | Time, location, activity, and mood-based personalization |
| 👤 Digital Nutrition Twin | Evolving behavioral fingerprint per user |
| 📊 Future Consequence Simulator | Project weight, energy, cravings 7–30 days forward |
| 📈 Weekly Insight Reports | Behavioral analytics and personal baseline comparison |

## Architecture

Microservices on Google Cloud Run:
- **API Gateway** — Node.js (Express) — public entry point
- **User Service** — Node.js — profiles + Digital Twin
- **Meal Service** — Node.js — logging + context capture
- **ML Service** — Python (FastAPI) — LSTM predictions + simulation
- **Insight Service** — Node.js — weekly reports
- **MongoDB** — persistent data store
- **Redis** — session cache + prediction cache

## Quick Start

### Prerequisites
- Docker + Docker Compose
- Node.js 20+
- Python 3.11+

### Run Locally

git clone https://github.com/your-org/nutrisphere-ai.git
cd nutrisphere-ai
cp .env.example .env
# Fill in values in .env
docker-compose up --build

API available at: http://localhost:3000

### System Architechture

nutrisphere-ai/
├── README.md
├── docker-compose.yml
├── .env.example
├── .gitignore
│
├── api-gateway/
│   ├── Dockerfile
│   ├── package.json
│   ├── src/
│   │   ├── index.js                # Express app entry
│   │   ├── middleware/
│   │   │   ├── auth.js             # JWT verification
│   │   │   ├── rateLimiter.js      # Redis-backed rate limiting
│   │   │   └── requestLogger.js
│   │   ├── routes/
│   │   │   ├── authRoutes.js
│   │   │   ├── mealRoutes.js
│   │   │   ├── predictRoutes.js
│   │   │   ├── simulateRoutes.js
│   │   │   ├── habitRoutes.js
│   │   │   ├── twinRoutes.js
│   │   │   └── insightRoutes.js
│   │   └── utils/
│   │       ├── serviceProxy.js     # Routes to microservices
│   │       └── errorHandler.js
│
├── services/
│   ├── user-service/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   └── src/
│   │       ├── index.js
│   │       ├── controllers/
│   │       │   ├── userController.js
│   │       │   └── twinController.js
│   │       ├── models/
│   │       │   ├── User.js         # Mongoose schema
│   │       │   └── NutritionTwin.js
│   │       └── services/
│   │           └── twinService.js  # Twin update logic
│   │
│   ├── meal-service/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   └── src/
│   │       ├── index.js
│   │       ├── controllers/
│   │       │   └── mealController.js
│   │       ├── models/
│   │       │   └── Meal.js
│   │       └── services/
│   │           ├── nutritionAnalyzer.js  # Food → macro lookup
│   │           └── contextCapture.js     # Context normalization
│   │
│   ├── insight-service/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   └── src/
│   │       ├── index.js
│   │       ├── controllers/
│   │       │   └── insightController.js
│   │       ├── models/
│   │       │   └── WeeklyReport.js
│   │       └── services/
│   │           └── reportGenerator.js
│
├── ml-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py                     # FastAPI entry point
│   ├── routers/
│   │   ├── prediction.py
│   │   ├── simulation.py
│   │   └── habits.py
│   ├── models/
│   │   ├── lstm_model.py           # Model architecture
│   │   ├── model_loader.py         # Load saved .h5 weights
│   │   └── saved_weights/
│   │       └── lstm_v1.h5
│   ├── services/
│   │   ├── predictor.py            # Inference logic
│   │   ├── simulator.py            # Future consequence logic
│   │   └── habit_analyzer.py       # Loop detection
│   ├── schemas/
│   │   ├── prediction_schema.py    # Pydantic models
│   │   └── simulation_schema.py
│   └── utils/
│       ├── feature_engineering.py
│       └── food_database.py        # Food → nutrition mapping
│
├── mobile-app/                     # React Native / Flutter
│   ├── src/
│   │   ├── screens/
│   │   │   ├── HomeScreen.jsx
│   │   │   ├── MealLogScreen.jsx
│   │   │   ├── SimulatorScreen.jsx
│   │   │   ├── HabitLoopsScreen.jsx
│   │   │   ├── TwinScreen.jsx
│   │   │   └── WeeklyInsightScreen.jsx
│   │   ├── components/
│   │   │   ├── InterventionCard.jsx
│   │   │   ├── FutureTimeline.jsx
│   │   │   ├── HabitLoopCard.jsx
│   │   │   └── TwinProfile.jsx
│   │   ├── store/                  # Redux / Zustand
│   │   └── api/
│   │       └── client.js
│
├── infrastructure/
│   ├── cloud-run/
│   │   └── deploy.sh               # Deployment script
│   ├── nginx/
│   │   └── nginx.conf
│   └── monitoring/
│       └── alerts.yaml
│
└── scripts/
    ├── seed_db.js                  # Seed MongoDB
    ├── train_model.py              # Train ML model
    └── generate_dummy_meals.py     # Synthetic data

### API Health Check

curl http://localhost:3000/health

### Run ML Service Standalone

cd ml-service
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

## Tech Stack

- **Frontend**: React Native (iOS + Android)
- **API Gateway**: Node.js + Express
- **Microservices**: Node.js + Express
- **ML Service**: Python + FastAPI + TensorFlow
- **Database**: MongoDB + Redis
- **Infrastructure**: Docker + Google Cloud Run
- **Auth**: JWT + bcrypt
- **Notifications**: Firebase Cloud Messaging

## Future Scope

- [ ] Wearable integration (Apple Watch, Fitbit) for biometric signals
- [ ] Voice-based meal logging via NLP
- [ ] Reinforcement learning for intervention personalization
- [ ] Social accountability features
- [ ] Integration with grocery apps for proactive shopping lists
- [ ] CGM (Continuous Glucose Monitor) data integration
- [ ] Multi-language support (Hindi, Spanish, Mandarin)

## License

MIT License — see [LICENSE](LICENSE)
