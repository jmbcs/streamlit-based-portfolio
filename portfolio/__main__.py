import os
import sys

# required to deploy app in streamlit
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


import streamlit as st

import portfolio.buttons
import portfolio.image
import portfolio.style
from portfolio.settings import config


def run():
    if "sidebar_state" not in st.session_state:
        st.session_state.sidebar_state = "collapsed"

    st.set_page_config(
        page_title="Portfolio - Júlio Silva",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state=st.session_state.sidebar_state,
    )

    # st.markdown(
    #     """

    # <span data-testid="collapsedControl">
    #     <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" class="eyeqlp51 st-emotion-cache-1pbsqtx ex0cdmw0">
    #         <path fill="none" d="M0 0h24v24H0V0z"></path>
    #         <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6-6-6z"></path>
    #     </svg>
    # </span>
    # """,
    #     unsafe_allow_html=True,
    # )

    # svg_code = """
    # <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" class="eyeqlp51 st-emotion-cache-1pbsqtx ex0cdmw0" style="width: 50px; height: 50px;">
    #     <path fill="none" d="M0 0h24v24H0V0z"></path>
    #     <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6-6-6z"></path>
    # </svg>
    # """

    # st.markdown(svg_code, unsafe_allow_html=True)

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

    # add button bar and logic for tabs
    portfolio.buttons.set_main_button_bar()

    # add divider at end
    st.markdown(config.html.structure_divider, unsafe_allow_html=True)

    # add footer with link to github code
    st.markdown(config.html.structure_footer, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
