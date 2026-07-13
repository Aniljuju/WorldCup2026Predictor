import joblib
import pandas as pd

# Load model
model = joblib.load("models/random_forest.pkl")

# Load encoders
team_encoder = joblib.load("models/team_encoder.pkl")
winner_encoder = joblib.load("models/winner_encoder.pkl")

print("✅ Model loaded successfully!")
print("✅ Team encoder loaded successfully!")
print("✅ Winner encoder loaded successfully!")


def predict_match(home_team, away_team):
    # Encode the team names
    home_encoded = team_encoder.transform([home_team])[0]
    away_encoded = team_encoder.transform([away_team])[0]

    # Create input for the model
    match = pd.DataFrame(
        [[home_encoded, away_encoded]],
        columns=["home_team", "away_team"]
    )

    # Predict the winner
    prediction = model.predict(match)
    probabilities = model.predict_proba(match)

    print("\nPrediction Probabilities:")
    for label, prob in zip(winner_encoder.classes_, probabilities[0]):
        print(f"{label}: {prob:.2%}")

    # Decode prediction
    result = winner_encoder.inverse_transform(prediction)[0]

    if result == "Home":
        return home_team
    elif result == "Away":
        return away_team
    else:
        return "Draw"


if __name__ == "__main__":
    home_team = input("Enter Home Team: ")
    away_team = input("Enter Away Team: ")

    winner = predict_match(home_team, away_team)

    print("\n🏆 Match Prediction")
    print(f"Home Team : {home_team}")
    print(f"Away Team : {away_team}")
    print(f"\nWinner: {winner}")