import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.buttons


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <h2 style='margin-left: 11.5vw;'>Main Tech Stack</h2>
                """,
                unsafe_allow_html=True,
            )

            portfolio.buttons.set_tech_stack_icons()
            st.markdown(
                config.html.skills,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.skills, quality="high")
