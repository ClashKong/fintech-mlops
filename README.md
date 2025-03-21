# 📊 FinTech MLOps: AI-gestützte Kreditbewertung

![GitHub Repo Stars](https://img.shields.io/github/stars/ClashKong/fintech-mlops?style=social)
![GitHub forks](https://img.shields.io/github/forks/ClashKong/fintech-mlops?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/ClashKong/fintech-mlops)

## 🚀 Projektziel
Ein **produktreifes KI-Modell**, das Banken hilft, Kreditrisiken zu bewerten! Dabei setzen wir auf moderne **MLOps-Technologien** wie **Docker, MLflow & FastAPI**. Perfekt für dein Portfolio! 🚀

---

## 📌 Features
✅ **ML-Modell**: Kreditbewertung mit Random Forest (Accuracy ~0.71)
✅ **MLOps**: MLflow zur Modellverwaltung & Experiment Tracking
✅ **Docker**: Vollständig containerisiert für einfache Bereitstellung
✅ **CI/CD-ready**: Automatisierung für Deployment & Tests (später!)
✅ **(Bald)**: REST API mit FastAPI + Cloud Deployment

---

## 📁 Projektstruktur
```
fintech-mlops/
│
├── data/               <- Datasets
├── notebooks/          <- Explorative Analysen
├── src/                <- Produktionscode
│   ├── model/          <- Modelltraining & MLflow
│   └── api/            <- (bald) FastAPI-Endpoints
│
├── Dockerfile          <- Docker-Konfiguration
├── requirements.txt    <- Python-Abhängigkeiten
├── .gitignore          <- Unnötige Dateien ignorieren
└── README.md           <- Diese Datei! 🚀
```

---

## 🔥 Schnellstart (Lokal)
### 1️⃣ Repository klonen
```bash
git clone https://github.com/ClashKong/fintech-mlops.git
cd fintech-mlops
```

### 2️⃣ Virtuelle Umgebung & Abhängigkeiten
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Modell trainieren (lokal)
```bash
python src/model/train_model.py
```

### 4️⃣ MLflow UI starten (optional)
```bash
mlflow ui --backend-store-uri file://$(pwd)/src/model/mlruns
```
Dann im Browser: **http://127.0.0.1:5000**

---

## 🐳 Docker-Setup
### 1️⃣ Docker-Image bauen
```bash
docker build -t fintech-mlops .
```

### 2️⃣ Container starten (Modelltraining)
```bash
docker run --rm fintech-mlops
```

### 3️⃣ MLflow UI im Container (optional)
```bash
docker run -p 5000:5000 fintech-mlops
```
Dann auf **http://127.0.0.1:5000** gehen.

---

## 🔜 Nächste Schritte
- [ ] **FastAPI-Endpoint bauen**: REST-API für Modell-Predictions 📡
- [ ] **Cloud Deployment**: Modell in AWS/GCP bereitstellen ☁️
- [ ] **CI/CD einrichten**: Automatische Tests & Deployment mit GitHub Actions 🔄

---

## 🤝 Mitwirken
Pull Requests sind willkommen! Starte das Projekt, wenn es dir gefällt ⭐

📩 **Kontakt**: [LinkedIn-Profil hier eintragen]

