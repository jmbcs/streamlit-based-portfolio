import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.buttons


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                config.html.about,
                unsafe_allow_html=True,
            )
            # st.markdown(
            #     """
            #     <h2 style='margin-left: 11.5vw;'>My Socials</h2>
            #     """,
            #     unsafe_allow_html=True,
            # )
            # portfolio.buttons.set_social_icons()

        with col2:
            st_lottie(config.animations.about, quality="high")
