from predict import predict_match


def simulate_round(teams, round_name):
    print(f"\n🏆 {round_name}\n")

    winners = []

    for i in range(0, len(teams), 2):
        home = teams[i]
        away = teams[i + 1]

        winner = predict_match(home, away, show_probabilities=False)

        print(f"{home} vs {away}")
        print(f"Winner: {winner}")
        print("-" * 40)

        winners.append(winner)

    return winners


# ============================================
# OFFICIAL WORLD CUP 2026 ROUND OF 32 TEAMS
# (ordered according to the knockout bracket)
# ============================================

teams = [
    "South Africa", "Canada",
    "Germany", "Paraguay",
    "Netherlands", "Morocco",
    "Brazil", "Japan",
    "France", "Sweden",
    "Norway", "Ivory Coast",
    "Mexico", "Ecuador",
    "England", "DR Congo",
    "United States", "Bosnia and Herzegovina",
    "Belgium", "Senegal",
    "Portugal", "Croatia",
    "Spain", "Austria",
    "Switzerland", "Algeria",
    "Australia", "Egypt",
    "Argentina", "Cape Verde",
    "Colombia", "Ghana"
]

# Round of 32 (32 -> 16)
round16 = simulate_round(teams, "Round of 32")

# Round of 16 (16 -> 8)
quarterfinals = simulate_round(round16, "Round of 16")

# Quarterfinals (8 -> 4)
semifinals = simulate_round(quarterfinals, "Quarterfinals")

# Semifinals (4 -> 2)
finalists = simulate_round(semifinals, "Semifinals")

# Final (2 -> 1)
champion = simulate_round(finalists, "Final")

print("\n" + "=" * 60)
print("🏆 FIFA WORLD CUP 2026")
print("=" * 60)
print(f"\n🥇 WORLD CHAMPION: {champion[0].upper()}")
print("=" * 60)