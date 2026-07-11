import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

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

# Combine all team names
all_teams = pd.concat([matches["home_team"], matches["away_team"]])

# Learn every team
team_encoder.fit(all_teams)

# Encode both columns
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

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Features:", X_train.shape)
print("Testing Features :", X_test.shape)

print()

print("Training Labels:", y_train.shape)
print("Testing Labels :", y_test.shape)

print("\nTraining the model...")

# Create the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))