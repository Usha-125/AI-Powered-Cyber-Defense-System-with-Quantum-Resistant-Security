import pandas as pd
data =pd.read_csv("network_data.csv")
print('full dataset')
print(data)
print(data.head(3))
print(data.info())
print("\n--- Features (X) ---")
X = data.drop("label", axis=1)
print(X)

print("\n--- Labels (Y) ---")
Y = data["label"]
print(Y)