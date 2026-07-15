import streamlit as st
from src.flags import get_flag_path


def match_card(home, away, winner):

    col1, col2 = st.columns([1, 5])

    with col1:
        flag = get_flag_path(home)
        if flag:
            st.image(flag, width=40)

    with col2:
        st.markdown(f"### {home}")

    st.write("🆚")

    col1, col2 = st.columns([1, 5])

    with col1:
        flag = get_flag_path(away)
        if flag:
            st.image(flag, width=40)

    with col2:
        st.markdown(f"### {away}")

    st.success(f"🏆 Winner: {winner}")

    st.divider()