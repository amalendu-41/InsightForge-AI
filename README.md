# 📊 AI-Powered BI Dashboard Generator

An AI-powered Business Intelligence platform that transforms raw CSV/Excel datasets into interactive dashboards with automated KPI detection, trend analysis, and AI-generated business insights using Ollama and Llama3.

---

## 🚀 Features

- Automated KPI, dimension, and date detection
- Interactive dashboard and chart generation
- AI-generated business summaries and recommendations
- FastAPI backend with Streamlit frontend
- SQLite-based lightweight persistence
- Local LLM integration using Ollama

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite |
| AI Engine | Ollama + Llama3 |
| Visualization | Plotly |
| Data Processing | Pandas |

---

## 📂 Project Structure

```bash
frontend/   → Streamlit UI
backend/    → APIs & business logic
uploads/    → Uploaded datasets
database/   → SQLite database
```

---

## ⚙️ Run Application

### 1️⃣ Start Backend

```bash
uvicorn backend.main:app --reload --reload-dir backend
```

### 2️⃣ Start Ollama

```bash
ollama run llama3
```

### 3️⃣ Start Frontend

```bash
streamlit run frontend/app.py
```

---

## 📈 Capabilities

✅ CSV/Excel Upload  
✅ Automated KPI Detection  
✅ Interactive Charts  
✅ AI Business Insights  
✅ Trend Analysis  
✅ FastAPI + Streamlit Architecture  
✅ SQLite Integration  

---

## 👨‍💻 Author

**Amalendu Kumar**  
Data Analyst | BI Developer | AI Analytics Enthusiast
