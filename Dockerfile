# Basis-Image mit Python
FROM python:3.9

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Dateien ins Container-Image
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Code ins Image
COPY src/ src/

# Starte das Training des Modells
CMD ["python", "src/model/train_model.py"]
