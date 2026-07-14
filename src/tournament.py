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

print("\n🏆 Round of 16\n")

round_of_16_winners = []

for i in range(0, len(winners), 2):

    home = winners[i]
    away = winners[i + 1]

    winner = predict_match(home, away)

    print(f"{home} vs {away}")
    print(f"Winner: {winner}")
    print("-" * 40)

    round_of_16_winners.append(winner)

print("\nTeams advancing to Quarterfinals")
print(round_of_16_winners)