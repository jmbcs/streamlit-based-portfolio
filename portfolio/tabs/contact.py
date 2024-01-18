import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.style
from portfolio.settings import config


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(config.html.contact_form, unsafe_allow_html=True)

            portfolio.style.set_style(path_to_style=config.styles.form)
        with col2:
            st_lottie(config.animations.contact, quality="high", speed=2)
