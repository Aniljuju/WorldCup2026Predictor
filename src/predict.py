import joblib

# Load model
model = joblib.load("models/random_forest.pkl")

# Load encoders
team_encoder = joblib.load("models/team_encoder.pkl")
winner_encoder = joblib.load("models/winner_encoder.pkl")

print("✅ Model loaded successfully!")
print("✅ Team encoder loaded successfully!")
print("✅ Winner encoder loaded successfully!")

home_team = input("Enter Home Team: ")
away_team = input("Enter Away Team: ")

# Encode the team names
home_encoded = team_encoder.transform([home_team])[0]
away_encoded = team_encoder.transform([away_team])[0]

print("\nEncoded Teams")
print(f"{home_team} -> {home_encoded}")
print(f"{away_team} -> {away_encoded}")