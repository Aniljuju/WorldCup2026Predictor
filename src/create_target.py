import pandas as pd

# Load the dataset
matches = pd.read_csv("data/raw/results.csv")

# Create the winner column
def get_winner(row):
    if row["home_score"] > row["away_score"]:
        return "Home"
    elif row["home_score"] < row["away_score"]:
        return "Away"
    else:
        return "Draw"

matches["winner"] = matches.apply(get_winner, axis=1)

# Show the first 10 rows
print(matches[["home_team", "away_team", "home_score", "away_score", "winner"]].head(10))