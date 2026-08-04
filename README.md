# 🤖 NexusNotify – AI-Powered Notification Intelligence System

> NexusNotify is an AI-powered notification intelligence platform that classifies, prioritizes, and explains notifications using Machine Learning, Semantic Retrieval, and Large Language Models (LLMs). It helps reduce notification fatigue by intelligently identifying phishing, transactional, promotional, and important notifications.

---

## 🚀 Problem Statement

Modern users receive hundreds of notifications every day, making it difficult to identify important messages while filtering spam, phishing attempts, and promotional content.

NexusNotify addresses this challenge by using AI to:

- Detect phishing notifications
- Prioritize important messages
- Reduce notification fatigue
- Explain every AI decision with supporting evidence

---

# ✨ Features

- 🔐 AI-powered Notification Classification
- 🧠 LLM-based Reasoning (Groq)
- 🔍 Semantic Similarity Retrieval
- 📊 Interactive Analytics Dashboard
- 📈 Evaluation Metrics (Accuracy, Precision, Recall, F1)
- ⚡ FastAPI REST Backend
- ⚛ React + TypeScript Frontend
- 📚 Explainable AI (Evidence Retrieval)
- 🔎 Search & Filter Notifications
- 📈 Confidence Analysis Charts

---

# 🏗 System Architecture

```
                Notification Dataset
                        │
                        ▼
              Context Builder Pipeline
                        │
                        ▼
              Feature Extraction Engine
                        │
                        ▼
             Rule-Based Decision Engine
                        │
                        ▼
           Semantic Evidence Retrieval
                        │
                        ▼
             Groq LLM Reasoning Engine
                        │
                        ▼
                Prediction Generator
                        │
                        ▼
               FastAPI REST Services
                        │
                        ▼
          React Analytics Dashboard
```

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Axios
- Recharts

## Backend

- FastAPI
- Python 3.13
- Pandas
- Scikit-learn
- Sentence Transformers

## AI / ML

- Groq LLM
- Semantic Embeddings
- Cosine Similarity
- Explainable AI
- Rule-Based Decision Engine

---

# 📂 Project Structure

```
NexusNotify
│
├── backend/
│   ├── app/
│   ├── pipelines/
│   ├── services/
│   ├── repositories/
│   └── api/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── hooks/
│   ├── pages/
│   └── api/
│
├── docs/
├── scripts/
├── output.csv
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone <repository-url>
cd NexusNotify
```

---

## Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirement.txt

uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger API:

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

# 📊 AI Workflow

```
Notification

      │

      ▼

Context Building

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

Groq LLM Reasoning

      │

      ▼

Final Prediction

      │

      ▼

Analytics Dashboard
```

---

# 📈 Dashboard Features

- Live Notification Predictions
- AI Decision Panel
- Confidence Scores
- Notification Type Distribution
- Analytics Charts
- Search Notifications
- Explainable AI Evidence

---

# 🔬 Evaluation Metrics

The system evaluates predictions using:

- Accuracy
- Precision
- Recall
- F1 Score

---

# 📸 Screenshots

Add screenshots here before submission.

- Dashboard
- AI Decision Panel
- Notification Analytics
- Search & Filter
- Evidence Panel

---

# 🔮 Future Enhancements

- Android Notification Integration
- Real-time Notification Monitoring
- Browser Extension
- Personalized User Learning
- Cloud Deployment
- Authentication & User Roles
- PostgreSQL Database
- Docker & Kubernetes Deployment

---

# 👨‍💻 Team

Hackathon Project

**Project Name:** NexusNotify

AI-Powered Personalized Notification Intelligence System

---

# 📄 License

This project is developed for educational and hackathon purposes.