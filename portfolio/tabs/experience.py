import streamlit as st
from streamlit_lottie import st_lottie

from portfolio.settings import config


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            # Convert content to HTML and apply styling to shift text 215px to the right
            st.markdown(
                config.html.experience,
                unsafe_allow_html=True,
            )
        with col2:
            st_lottie(config.animations.experience, quality="high")
