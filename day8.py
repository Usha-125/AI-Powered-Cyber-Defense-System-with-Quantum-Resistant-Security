import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

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

# New incoming network activity (simulated)
new_data = pd.DataFrame([{
    "duration": 1,
    "protocol": "ICMP",
    "bytes": 40,
    "flag": "REJ"
}])

# Encode new data
for col in ["protocol", "flag"]:
    new_data[col] = encoder.fit_transform(new_data[col])

# Predict
prediction = model.predict(new_data)[0]

# IDS Logic
if prediction == 1:
    print("⚠️ ALERT: Intrusion Detected! Possible Attack.")
else:
    print("✅ Normal Activity. System is Safe.")
