import json

import streamlit as st
from streamlit_lottie import st_lottie

with open("portfolio/animation/about.json") as source:
    ABOUT_ANIMATION = json.load(source)


def set_about_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("27 Year old")
            st.subheader("🇵🇹 Portuguese")

            st.write("------")
            st.subheader("Hobbies")

            st.code(
                body="""   
                    \n      📖 Reading
                    \n      🎮 Videogames
                    \n      💻 Coding 
                    \n      💪 Gym
                    \n      🎵 Music 
                    \n      🌇 Travelling
                    \n      💵 Finances & Investing
                    """
            )

        with col2:
            st_lottie(ABOUT_ANIMATION, height=700, width=900)
