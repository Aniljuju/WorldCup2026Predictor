from predict import predict_match


def simulate_round(teams, round_name):
    print(f"\n🏆 {round_name}\n")

    winners = []

    for i in range(0, len(teams), 2):
        home = teams[i]
        away = teams[i + 1]

        winner = predict_match(home, away)

        print(f"{home} vs {away}")
        print(f"Winner: {winner}")
        print("-" * 40)

        winners.append(winner)

    return winners


# ----------------------------
# Official Round of 32 (for now use a sample)
# ----------------------------

round_of_32 = [
    "South Africa", "Canada",
    "Germany", "Paraguay",
    "Netherlands", "Morocco",
    "Brazil", "Japan"
]

# Round of 32
round16 = simulate_round(round_of_32, "Round of 32")

# Round of 16
quarterfinals = simulate_round(round16, "Round of 16")

print("\nTeams advancing to Quarterfinals")
print(quarterfinals)