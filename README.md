# 🤖 NexusNotify

<div align="center">

### 🧠 AI-Powered Personalized Notification Intelligence System

*Classify • Prioritize • Explain • Protect*

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Render-Backend-46E3B7?style=for-the-badge&logo=render)

</div>

---

## 🌍 Live Demo

| Service | URL |
|----------|-----|
| 🚀 Frontend | **https://nexus-notify-delta.vercel.app/** |
| ⚡ Backend API | **https://nexusnotify.onrender.com** |
| 📚 Swagger Docs | **https://nexusnotify.onrender.com/docs** |

---

# 📖 Overview

NexusNotify is an AI-powered notification intelligence platform that analyzes incoming notifications, predicts their importance, detects phishing attempts, and provides explainable AI decisions with supporting evidence.

The system combines:

- 🤖 Large Language Models (Groq Llama 3.3)
- 🧠 Rule-Based Decision Engine
- 🔍 Semantic Retrieval
- 📊 Interactive Analytics Dashboard
- 📚 Explainable AI

to reduce notification fatigue while ensuring important messages are never missed.

---

# ✨ Features

✅ AI Notification Classification

✅ Phishing Detection

✅ Personalized Notification Prioritization

✅ Groq LLM Reasoning Engine

✅ Explainable AI with Evidence Retrieval

✅ Analytics Dashboard

✅ Search & Filter Notifications

✅ REST APIs with Swagger Documentation

✅ Production Deployment

---

# 🏗 Architecture

```text
                  📱 Notification Dataset
                            │
                            ▼
               🧩 Context Builder Pipeline
                            │
                            ▼
                ⚙ Feature Extraction Engine
                            │
                            ▼
              🧠 Rule-Based Decision Engine
                            │
                            ▼
          🔍 Semantic Evidence Retrieval
                            │
                            ▼
              🤖 Groq LLM Reasoning Engine
                            │
                            ▼
                📄 Prediction Generator
                            │
                            ▼
                 ⚡ FastAPI REST API
                            │
                            ▼
         ⚛ React + TypeScript Dashboard
```

---

# 🛠 Tech Stack

## 💻 Frontend

- ⚛ React
- 🔷 TypeScript
- ⚡ Vite
- Axios
- Recharts

## ⚙ Backend

- 🐍 Python
- ⚡ FastAPI
- Pandas
- NumPy
- Scikit-learn
- Pydantic
- SQLAlchemy

## 🤖 AI & Machine Learning

- Groq Llama 3.3 70B
- Semantic Embeddings
- Cosine Similarity
- Rule-Based Decision Engine
- Explainable AI

---

# 📊 Dashboard

The analytics dashboard provides:

- 📈 Accuracy
- 🎯 Precision
- 📊 Recall
- 🏆 F1 Score
- 📩 Notification Predictions
- 🤖 AI Decision Panel
- 🔎 Search & Filtering
- 📚 Evidence Retrieval
- 📉 Confidence Distribution
- 📊 Notification Type Analytics

---

# 📈 AI Workflow

```text
Notification

      │

      ▼

Context Builder

      │

      ▼

Feature Extraction

      │

      ▼

Rule-Based Prediction

      │

      ▼

Semantic Retrieval

      │

      ▼

Groq LLM

      │

      ▼

Final Prediction

      │

      ▼

Dashboard Visualization
```

---

# 📡 REST API

| Endpoint | Description |
|------------|-------------|
| `/messages/` | List notifications |
| `/prediction/{message_id}` | Predict notification |
| `/predictions/` | All predictions |
| `/metrics/` | Evaluation metrics |
| `/features/{message_id}` | Feature extraction |
| `/context/{message_id}` | Notification context |
| `/debug/message/{message_id}` | Debug endpoint |
| `/health` | Health check |

Swagger Documentation:

```
https://nexusnotify.onrender.com/docs
```

---

# 📂 Project Structure

```text
NexusNotify
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── config/
│   │   ├── evaluation/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── pipelines/
│   │   └── models/
│   │
│   ├── datasets/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   └── types/
│   │
│   └── package.json
│
├── output.csv
└── README.md
```

---

# ⚙ Local Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NexusNotify.git

cd NexusNotify
```

---

## Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# 📊 Model Evaluation

Current Evaluation Metrics

| Metric | Score |
|---------|------:|
| Accuracy | **100%** |
| Precision | **100%** |
| Recall | **100%** |
| F1 Score | **100%** |

---


# 🚀 Deployment

## Frontend

▲ Vercel

## Backend

⚡ Render

## API Documentation

FastAPI Swagger UI

---

# 🔮 Future Enhancements

- 📱 Android Notification Integration
- 🔔 Real-Time Notification Monitoring
- ☁ PostgreSQL Database
- 👥 Multi-User Support
- 🔐 Authentication & Authorization
- 📈 Personalized Learning
- 🐳 Docker Deployment
- ☸ Kubernetes Support
- 📊 Advanced Analytics

---

# 👨‍💻 Author

**Vinumahanthesh G**

AI & Machine Learning Engineer

- 💼 LinkedIn: *https://www.linkedin.com/in/mahantheshvinu*
- 🐙 GitHub: *https://github.com/MAHANTHESHVINU*

---

# 📄 License

This project was developed for educational and hackathon purposes.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with ❤️ using FastAPI, React, TypeScript & AI**

</div>