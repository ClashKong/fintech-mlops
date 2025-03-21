import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import os


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
columns = [
    "Status", "Duration", "CreditHistory", "Purpose", "CreditAmount", "Savings", "EmploymentSince",
    "InstallmentRate", "PersonalStatusSex", "OtherDebtors", "ResidenceSince", "Property",
    "Age", "OtherInstallmentPlans", "Housing", "ExistingCredits", "Job", "LiablePeople",
    "Telephone", "ForeignWorker", "Target"
]
df = pd.read_csv(url, sep=' ', names=columns)
df["Target"] = df["Target"].apply(lambda x: 1 if x == 1 else 0)


df = df.dropna()
df = pd.get_dummies(df.select_dtypes(include=[int, float]), drop_first=True)

X = df.drop("Target", axis=1)
y = df["Target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


mlflow.set_tracking_uri("file:///" + os.path.abspath("src/model/mlruns").replace("\\", "/"))
mlflow.set_experiment("credit-risk-model")


with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

    print(f"✅ Modell trainiert! Accuracy: {acc:.4f}")

