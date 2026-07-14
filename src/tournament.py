from predict import predict_match

print("🏆 FIFA World Cup 2026 - Round of 32\n")

round_of_32 = [
    ("South Africa", "Canada"),
    ("Germany", "Paraguay"),
    ("Netherlands", "Morocco"),
    ("Brazil", "Japan"),
]

winners = []

for home, away in round_of_32:
    print(f"\n{home} vs {away}")

    winner = predict_match(home, away)

    print(f"Winner: {winner}")
    print("-" * 40)

    winners.append(winner)

print("\n🏆 Teams advancing to the Round of 16")
print(winners)