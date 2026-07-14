import streamlit as st
from src.tournament import simulate_tournament

st.set_page_config(
    page_title="FIFA World Cup 2026 Predictor",
    page_icon="⚽",
    layout="centered"
)

# Sidebar
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "⚽ Match Predictor",
        "🏆 Tournament Simulator",
        "ℹ About"
    ]
)

# ---------------- HOME ----------------
if page == "🏠 Home":

    st.title("⚽ FIFA World Cup 2026 Predictor")

    st.write("""
    Predict FIFA World Cup 2026 knockout matches using
    a Machine Learning model trained on historical international matches.
    """)

    st.markdown("---")

    st.header("Features")

    st.write("✅ Predict a single match")
    st.write("✅ Simulate the entire knockout tournament")
    st.write("✅ View prediction probabilities")

# ---------------- MATCH ----------------
elif page == "⚽ Match Predictor":

    st.title("⚽ Match Predictor")

    st.info("Coming in the next step!")

# ---------------- TOURNAMENT ----------------
elif page == "🏆 Tournament Simulator":

    st.title("🏆 FIFA World Cup 2026 Tournament Simulator")

    st.write("Click the button below to simulate the entire knockout tournament.")

    if st.button("🏆 Simulate Tournament"):

        tournament = simulate_tournament()

        for round_name in [
            "Round of 32",
            "Round of 16",
            "Quarterfinals",
            "Semifinals",
            "Final"
        ]:

            st.subheader(round_name)

            for match in tournament[round_name]:

                st.write(
                    f"**{match['home']}** vs **{match['away']}**"
                )

                st.success(f"Winner: {match['winner']}")

        st.markdown("---")

        st.header("🏆 FIFA World Cup Champion")

        st.balloons()

        st.success(f"🥇 {tournament['Champion']}")

# ---------------- ABOUT ----------------
else:

    st.title("ℹ About")

    st.write("""
    Developed using:

    - Python
    - Pandas
    - Scikit-learn
    - Streamlit

    Dataset:
    International football results
    """)