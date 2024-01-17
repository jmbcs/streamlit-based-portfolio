from pathlib import Path

import streamlit as st


def set_style(path_to_style: Path):
    # CSS styles file
    with open(path_to_style) as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)
