import os
import sys

import streamlit as st

# required to deploy app in streamlit
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import portfolio.buttons
import portfolio.image
import portfolio.style
from portfolio.settings import config


def run():
    st.set_page_config(
        page_title="Porfolio - Júlio Silva", page_icon="💼", layout="wide"
    )
    # set the styles
    portfolio.style.set_style(path_to_style=config.styles.main)
    st.markdown(config.html.stucture_style, unsafe_allow_html=True)

    portfolio.image.set_profile_image()

    # Top title (name)
    st.markdown(
        config.html.structure_title,
        unsafe_allow_html=True,
    )

    # Second title (profession)
    st.write(
        config.html.structure_subtitle,
        unsafe_allow_html=True,
    )

    # Set the tech stack under subtitle
    st.markdown(config.html.structure_tech_stack, unsafe_allow_html=True)

    # add a divider
    st.markdown(config.html.structure_divider, unsafe_allow_html=True)

    # add button bar and logic for tabs
    portfolio.buttons.set_main_button_bar()

    # add divider at end
    st.markdown(config.html.structure_divider, unsafe_allow_html=True)

    # add footer with link to github code
    st.markdown(config.html.structure_footer, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
