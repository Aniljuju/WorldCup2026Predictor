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


def predict_match(home_team, away_team, show_probabilities=True):

    # Encode teams
    home_encoded = team_encoder.transform([home_team])[0]
    away_encoded = team_encoder.transform([away_team])[0]

    # Create dataframe
    match = pd.DataFrame(
        [[home_encoded, away_encoded]],
        columns=["home_team", "away_team"]
    )

    # Predict
    prediction = model.predict(match)
    probabilities = model.predict_proba(match)

    # Show probabilities only if requested
    if show_probabilities:
        print("\nPrediction Probabilities:")
        for label, prob in zip(winner_encoder.classes_, probabilities[0]):
            print(f"{label}: {prob:.2%}")

    # Decode result
    result = winner_encoder.inverse_transform(prediction)[0]

    if result == "Home":
        return home_team

    elif result == "Away":
        return away_team

    else:
        # Knockout tie-break
        home_prob = probabilities[0][list(winner_encoder.classes_).index("Home")]
        away_prob = probabilities[0][list(winner_encoder.classes_).index("Away")]

        if show_probabilities:
            print("\nMatch drawn after 90 minutes.")
            print("Penalty Shootout decides the winner!")

        if home_prob >= away_prob:
            return home_team
        else:
            return away_team


if __name__ == "__main__":

    home_team = input("Enter Home Team: ")
    away_team = input("Enter Away Team: ")

    winner = predict_match(home_team, away_team)

    print("\n🏆 Match Prediction")
    print(f"Home Team : {home_team}")
    print(f"Away Team : {away_team}")
    print(f"Winner    : {winner}")