import random
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


def predict_match(home_team, away_team, show_probabilities=True, random_mode=False):

    home_encoded = team_encoder.transform([home_team])[0]
    away_encoded = team_encoder.transform([away_team])[0]

    match = pd.DataFrame(
        [[home_encoded, away_encoded]],
        columns=["home_team", "away_team"]
    )

    probabilities = model.predict_proba(match)[0]

    labels = list(winner_encoder.classes_)

    home_prob = probabilities[labels.index("Home")]
    draw_prob = probabilities[labels.index("Draw")]
    away_prob = probabilities[labels.index("Away")]

    if show_probabilities:
        print("\nPrediction Probabilities:")
        print(f"Home : {home_prob:.2%}")
        print(f"Draw : {draw_prob:.2%}")
        print(f"Away : {away_prob:.2%}")

    # -----------------------
    # NORMAL MODE
    # -----------------------

    if not random_mode:

        prediction = model.predict(match)[0]
        result = winner_encoder.inverse_transform([prediction])[0]

        if result == "Home":
            return home_team

        elif result == "Away":
            return away_team

        else:
            # knockout draw
            if home_prob >= away_prob:
                return home_team
            else:
                return away_team

    # -----------------------
    # RANDOM TOURNAMENT MODE
    # -----------------------

    outcome = random.choices(
        ["Home", "Draw", "Away"],
        weights=[home_prob, draw_prob, away_prob],
        k=1
    )[0]

    if outcome == "Home":
        return home_team

    elif outcome == "Away":
        return away_team

    else:
        # simulate penalties

        penalty_winner = random.choices(
            [home_team, away_team],
            weights=[home_prob, away_prob],
            k=1
        )[0]

        return penalty_winner


if __name__ == "__main__":

    home_team = input("Home Team: ")
    away_team = input("Away Team: ")

    winner = predict_match(
        home_team,
        away_team,
        show_probabilities=True,
        random_mode=False
    )

    print("\nWinner:", winner)