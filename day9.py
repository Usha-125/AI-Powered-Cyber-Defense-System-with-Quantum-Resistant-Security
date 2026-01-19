import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime

# Load and encode dataset
data = pd.read_csv("network_data.csv")

encoder = LabelEncoder()
for col in ["protocol", "flag", "label"]:
    data[col] = encoder.fit_transform(data[col])

X = data.drop("label", axis=1)
Y = data["label"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, Y)

# New incoming network activity
new_activity = {
    "duration": 1,
    "protocol": "ICMP",
    "bytes": 40,
    "flag": "REJ"
}

new_data = pd.DataFrame([new_activity])

# Encode new data
for col in ["protocol", "flag"]:
    new_data[col] = encoder.fit_transform(new_data[col])

# Predict
prediction = model.predict(new_data)[0]

# IDS Logic with detailed alert
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if prediction == 1:
    alert = f"""
--- SECURITY ALERT ---
Time      : {current_time}
Type      : Intrusion Detected
Details   : {new_activity}
Severity  : HIGH
Action    : Investigate Immediately
----------------------
"""
    print(alert)
else:
    print("System Status: Normal activity detected. No threat.")
