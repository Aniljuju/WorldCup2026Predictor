import base64
import os
from src.flags import get_flag_path

_flag_cache = {}
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def world_cup_logo():
    logo_path = os.path.join(
        _PROJECT_ROOT,
        "assets",
        "images",
        "2026WC.png"
    )

    try:
        with open(logo_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()

        return f'''
        <img
            class="wc-logo"
            src="data:image/png;base64,{b64}"
        >
        '''

    except FileNotFoundError:
        return ""


def flag_img(team):
    if team not in _flag_cache:

        rel_path = get_flag_path(team)

        if not rel_path:
            _flag_cache[team] = ""

        else:
            abs_path = os.path.join(_PROJECT_ROOT, rel_path)

            try:
                with open(abs_path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()

                _flag_cache[team] = f'''
                <img
                    class="flag"
                    src="data:image/svg+xml;base64,{b64}"
                    width="22">
                '''

            except FileNotFoundError:
                _flag_cache[team] = ""

    return _flag_cache[team]


def team_row(name, is_winner):

    cls = "team winner" if is_winner else "team"

    return f'''
    <div class="{cls}">
        {flag_img(name)}
        <span class="nm">{name}</span>
    </div>
    '''


def match_box(match, side):

    home = match["home"]
    away = match["away"]
    winner = match["winner"]

    return f'''
    <div class="match {side}">
        {team_row(home, home == winner)}
        <div class="divider"></div>
        {team_row(away, away == winner)}
    </div>
    '''


def column(matches, side, round_class):

    boxes = "\n".join(
        match_box(match, side)
        for match in matches
    )

    return f'''
    <div class="round {round_class} {side}">
        {boxes}
    </div>
    '''


def generate_bracket(tournament):

    r32 = tournament["Round of 32"]
    r16 = tournament["Round of 16"]
    qf = tournament["Quarterfinals"]
    sf = tournament["Semifinals"]

    final = tournament["Final"][0]
    champion = tournament["Champion"]

    left_r32 = r32[:8]
    right_r32 = r32[8:]

    left_r16 = r16[:4]
    right_r16 = r16[4:]

    left_qf = qf[:2]
    right_qf = qf[2:]

    left_sf = sf[:1]
    right_sf = sf[1:]

    final_box = match_box(final, "final")

    bracket_html = f'''
    <div class="bracket-wrap">

        <div class="side-block">
            {column(left_r32,"left","col-r32")}
            {column(left_r16,"left","col-r16")}
            {column(left_qf,"left","col-qf")}
            {column(left_sf,"left","col-sf")}
        </div>

        <div class="center-block">

            <div class="round col-final">
                {final_box}
            </div>

            <div class="trophy-wrap">

                <div class="trophy-icon">
                    {world_cup_logo()}
                </div>

                <div class="champion-label">
                    CHAMPION
                </div>

                <div class="champion-box">
                    {flag_img(champion)}
                    <span class="nm">
                        {champion}
                    </span>
                </div>

            </div>

        </div>

        <div class="side-block reverse">
            {column(right_sf,"right","col-sf")}
            {column(right_qf,"right","col-qf")}
            {column(right_r16,"right","col-r16")}
            {column(right_r32,"right","col-r32")}
        </div>

    </div>
    '''

    return f'''
    <div class="poster">

        <div class="header">

            <div class="trophy-icon">
                {world_cup_logo()}
            </div>

            <h1>
                WORLD CUP BRACKET
            </h1>

            <div class="subtitle">
                ROUND OF 32 &middot; PREDICTED RESULTS
            </div>

        </div>

        {bracket_html}

        <div class="broadcaster">
            FIFA WORLD CUP 2026 &nbsp;|&nbsp; PREDICTOR BRACKET
        </div>

    </div>

    <div class="bottom-bar"></div>
    '''