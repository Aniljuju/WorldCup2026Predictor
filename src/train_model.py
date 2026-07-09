import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
matches = pd.read_csv("data/raw/results.csv")


# Create winner column
def get_winner(row):
    if row["home_score"] > row["away_score"]:
        return "Home"
    elif row["home_score"] < row["away_score"]:
        return "Away"
    else:
        return "Draw"


matches["winner"] = matches.apply(get_winner, axis=1)

# Encode teams
team_encoder = LabelEncoder()

all_teams = pd.concat([matches["home_team"], matches["away_team"]])
team_encoder.fit(all_teams)

matches["home_team"] = team_encoder.transform(matches["home_team"])
matches["away_team"] = team_encoder.transform(matches["away_team"])

# Encode winner
winner_encoder = LabelEncoder()
matches["winner"] = winner_encoder.fit_transform(matches["winner"])

# -----------------------------
# Features (X)
# -----------------------------
X = matches[["home_team", "away_team"]]

# -----------------------------
# Target (y)
# -----------------------------
y = matches["winner"]

print("Features (X)")
print(X.head())

print("\nTarget (y)")
print(y.head())