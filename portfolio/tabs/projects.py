import streamlit as st
from settings import config
from streamlit_lottie import st_lottie


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#\n" * 20)
        with col2:
            st_lottie(config.animations.computer, height=700, width=900)
