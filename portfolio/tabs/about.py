import streamlit as st
from settings import config
from streamlit_lottie import st_lottie


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                config.html.about,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.about, height=500, width=600, quality="high")
