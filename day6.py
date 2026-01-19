import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv("network_data.csv")

# Encode categorical columns properly
encoders = {}
categorical_cols = ["protocol", "flag", "label"]

for col in categorical_cols:
    encoders[col] = LabelEncoder()
    data[col] = encoders[col].fit_transform(data[col])

# Split X and Y
X = data.drop("label", axis=1)
Y = data["label"]

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

# Predict
Y_pred = model.predict(X_test)

# Evaluate
acc = accuracy_score(Y_test, Y_pred)
cm = confusion_matrix(Y_test, Y_pred)

print("Predicted:", Y_pred)
print("Actual:   ", list(Y_test))
print("Accuracy:", acc)
print("\nConfusion Matrix:\n", cm)
