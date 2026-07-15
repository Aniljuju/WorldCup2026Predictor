from pathlib import Path

# Folder containing all SVG flags
FLAGS_FOLDER = Path("assets/flags")


TEAM_FLAGS = {
    "Algeria": "dz.svg",
    "Argentina": "ar.svg",
    "Australia": "au.svg",
    "Austria": "at.svg",
    "Belgium": "be.svg",
    "Bosnia and Herzegovina": "ba.svg",
    "Brazil": "br.svg",
    "Canada": "ca.svg",
    "Cape Verde": "cv.svg",
    "Colombia": "co.svg",
    "DR Congo": "cd.svg",
    "Ecuador": "ec.svg",
    "Egypt": "eg.svg",
    "England": "gb-eng.svg",
    "France": "fr.svg",
    "Germany": "de.svg",
    "Ghana": "gh.svg",
    "Ivory Coast": "ci.svg",
    "Japan": "jp.svg",
    "Mexico": "mx.svg",
    "Morocco": "ma.svg",
    "Netherlands": "nl.svg",
    "Norway": "no.svg",
    "Paraguay": "py.svg",
    "Portugal": "pt.svg",
    "Senegal": "sn.svg",
    "South Africa": "za.svg",
    "Spain": "es.svg",
    "Sweden": "se.svg",
    "Switzerland": "ch.svg",
    "United States": "us.svg"
}


def get_flag_path(team):
    filename = TEAM_FLAGS.get(team)

    if filename is None:
        return None

    return str(FLAGS_FOLDER / filename)