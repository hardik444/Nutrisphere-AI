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
