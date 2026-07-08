import pandas as pd

# Load the dataset
matches = pd.read_csv("data/raw/results.csv")

# First 5 rows
print("===== First 5 Matches =====")
print(matches.head())

# Dataset size
print("\n===== Shape =====")
print(matches.shape)

# Column names
print("\n===== Columns =====")
print(matches.columns.tolist())

# Data types
print("\n===== Data Types =====")
print(matches.dtypes)

# Missing values
print("\n===== Missing Values =====")
print(matches.isnull().sum())