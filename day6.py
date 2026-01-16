# ===============================
# Day 6: Machine Learning Model
# AI-Powered Cyber Defense System
# ===============================

import pandas as pd

# sklearn (scikit-learn) modules
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# -------------------------------
# 1. Load the dataset
# -------------------------------
data = pd.read_csv("network_data.csv")
print("Original Data:\n")
print(data)

# -------------------------------
# 2. Encode categorical columns
# -------------------------------
# We create a SEPARATE encoder for each column
encoders = {}

categorical_columns = ["protocol", "flag", "label"]

for col in categorical_columns:
    encoders[col] = LabelEncoder()
    data[col] = encoders[col].fit_transform(data[col])

print("\nEncoded Data:\n")
print(data)

# -------------------------------
# 3. Separate features and label
# -------------------------------
X = data.drop("label", axis=1)   # input features
Y = data["label"]                # output class

# -------------------------------
# 4. Split data into train & test
# -------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,       # 30% test data
    random_state=42       # same result every run
)

# -------------------------------
# 5. Train Decision Tree model
# -------------------------------
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# -------------------------------
# 6. Make predictions
# -------------------------------
predictions = model.predict(X_test)

# -------------------------------
# 7. Evaluate the model
# -------------------------------
accuracy = accuracy_score(Y_test, predictions)

print("\nPredicted Labels :", predictions)
print("Actual Labels    :", list(Y_test))
print("Model Accuracy   :", accuracy)
