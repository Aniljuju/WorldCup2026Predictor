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
    return "Draw"

matches["winner"] = matches.apply(get_winner, axis=1)

# Create team encoder
team_encoder = LabelEncoder()

# Combine all team names (home + away)
all_teams = pd.concat([matches["home_team"], matches["away_team"]])

# Learn every unique team
team_encoder.fit(all_teams)

# Encode both columns
matches["home_team"] = team_encoder.transform(matches["home_team"])
matches["away_team"] = team_encoder.transform(matches["away_team"])

# Create winner encoder
winner_encoder = LabelEncoder()

# Encode the winner column
matches["winner"] = winner_encoder.fit_transform(matches["winner"])

# Display the first 10 rows
print("\nEncoded Dataset:")
print(matches[["home_team", "away_team", "winner"]].head(10))