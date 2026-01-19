import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
from cryptography.fernet import Fernet

# 1. Load and prepare dataset
data = pd.read_csv("network_data.csv")

encoder = LabelEncoder()
for col in ["protocol", "flag", "label"]:
    data[col] = encoder.fit_transform(data[col])

X = data.drop("label", axis=1)
Y = data["label"]

# 2. Train AI model
model = DecisionTreeClassifier()
model.fit(X, Y)

# 3. New incoming network activity (simulate)
new_activity = {
    "duration": 1,
    "protocol": "ICMP",
    "bytes": 40,
    "flag": "REJ"
}

new_data = pd.DataFrame([new_activity])

for col in ["protocol", "flag"]:
    new_data[col] = encoder.fit_transform(new_data[col])

# 4. Predict using AI
prediction = model.predict(new_data)[0]

# 5. IDS Logic
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
    print("⚠️ Attack Detected!")
    print("\nOriginal Alert:\n", alert)

    # 6. Quantum-Safe Encryption (Simulated)
    key = Fernet.generate_key()
    cipher = Fernet(key)

    encrypted_alert = cipher.encrypt(alert.encode())
    print("\nEncrypted Alert (Secure):\n", encrypted_alert)

    decrypted_alert = cipher.decrypt(encrypted_alert).decode()
    print("\nDecrypted Alert (For Admin):\n", decrypted_alert)

else:
    print("✅ Normal Activity. System is Safe.")
