from src.flags import get_flag_path


def generate_match_html(home, away, winner):
    home_flag = get_flag_path(home)
    away_flag = get_flag_path(away)

    return f"""
    <div class="match">

        <div class="team">
            <img src="{home_flag}">
            <span>{home}</span>
        </div>

        <div class="vs">
            VS
        </div>

        <div class="team">
            <img src="{away_flag}">
            <span>{away}</span>
        </div>

        <div class="winner">
            🏆 Winner: {winner}
        </div>

    </div>
    """


def generate_round_html(round_name, matches):

    html = f"""
    <div class="round">
        <div class="round-title">{round_name}</div>
    """

    for match in matches:
        html += generate_match_html(
            match["home"],
            match["away"],
            match["winner"]
        )

    html += "</div>"

    return html


def generate_bracket(tournament):

    html = '<div class="bracket">'

    rounds = [
        "Round of 32",
        "Round of 16",
        "Quarterfinals",
        "Semifinals",
        "Final"
    ]

    for round_name in rounds:
        html += generate_round_html(
            round_name,
            tournament[round_name]
        )

    html += "</div>"

    html += f"""
    <div class="champion">

        <h2>🏆 Champion</h2>

        <h1>{tournament['Champion']}</h1>

    </div>
    """

    return html