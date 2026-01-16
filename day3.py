import pandas as pd

# Load the dataset
data = pd.read_csv("network_data.csv")
print("Dataset Loaded Successfully!\n")
print(data)

# Separate features (X) and labels (Y)
X = data.drop("label", axis=1)
Y = data["label"]

print("\n--- Features (X) ---")
print(X)

print("\n--- Labels (Y) ---")
print(Y)

print("\nNumber of records:", len(data))
print("Number of features:", X.shape[1])
