from pathlib import Path

import streamlit as st
from settings import config


def set_style(path_to_style: Path = config.style_path):
    # CSS styles file
    with open(path_to_style, mode="r") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)
