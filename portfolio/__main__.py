import streamlit as st

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
    st.markdown(config.html.style, unsafe_allow_html=True)

    portfolio.image.set_profile_image()

    # Top title
    st.markdown(
        config.html.title,
        unsafe_allow_html=True,
    )

    # Subtitle
    st.write(
        config.html.subtitle,
        unsafe_allow_html=True,
    )

    portfolio.buttons.set_social_icons()

    # Displaying Markdown with icons

    st.markdown(config.html.divider, unsafe_allow_html=True)

    portfolio.buttons.set_main_button_bar()

    st.markdown(config.html.divider, unsafe_allow_html=True)

    st.markdown(config.html.footer, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
