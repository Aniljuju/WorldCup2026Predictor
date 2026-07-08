import pandas as pd
# Load the dataset
matches = pd.read_csv("data/raw/results.csv")

# Show first 5 rows
print(matches.head())

print("\nDataset Shape:")
print(matches.shape)

print("\nColumn Names:")
print(matches.columns)