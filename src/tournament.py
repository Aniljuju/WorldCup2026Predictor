from src.predict import predict_match


def simulate_round(teams, round_name):
    winners = []
    matches = []

    for i in range(0, len(teams), 2):
        home = teams[i]
        away = teams[i + 1]

        winner = predict_match(
            home,
            away,
            show_probabilities=False,
            random_mode=True
        )

        matches.append({
            "home": home,
            "away": away,
            "winner": winner
        })

        winners.append(winner)

    return winners, matches


def simulate_tournament():

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

    tournament = {}

    # Round of 32
    round16, tournament["Round of 32"] = simulate_round(
        teams,
        "Round of 32"
    )

    # Round of 16
    quarterfinals, tournament["Round of 16"] = simulate_round(
        round16,
        "Round of 16"
    )

    # Quarterfinals
    semifinals, tournament["Quarterfinals"] = simulate_round(
        quarterfinals,
        "Quarterfinals"
    )

    # Semifinals
    finalists, tournament["Semifinals"] = simulate_round(
        semifinals,
        "Semifinals"
    )

    # Final
    champion, tournament["Final"] = simulate_round(
        finalists,
        "Final"
    )

    tournament["Champion"] = champion[0]

    return tournament


if __name__ == "__main__":

    tournament = simulate_tournament()

    for round_name in [
        "Round of 32",
        "Round of 16",
        "Quarterfinals",
        "Semifinals",
        "Final"
    ]:

        print(f"\n🏆 {round_name}\n")

        for match in tournament[round_name]:
            print(f"{match['home']} vs {match['away']}")
            print(f"Winner: {match['winner']}")
            print("-" * 40)

    print("\n" + "=" * 50)
    print("🏆 FIFA WORLD CUP 2026 CHAMPION 🏆")
    print("=" * 50)
    print(f"\nChampion: {tournament['Champion']}")