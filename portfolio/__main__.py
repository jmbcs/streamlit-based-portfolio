import streamlit as st
from settings import config

import portfolio.buttons
import portfolio.image
import portfolio.style


def run():
    st.set_page_config(
        page_title="Júlio Silva's Porfolio", page_icon="💻", layout="wide"
    )

    portfolio.style.set_style(path_to_style=config.styles.main)

    portfolio.image.set_profile_image()

    # Top title
    st.markdown(
        "<h1 style='text-align: center; color: #ffffff;'>Júlio Silva</h1>",
        unsafe_allow_html=True,
    )

    # Subtitle
    st.write(
        f"""<div class="subtitle" style="text-align: center;color: #ff4c4c;">Backend Enginer / Data Analyst</div>""",
        unsafe_allow_html=True,
    )

    portfolio.buttons.set_social_icons()

    st.divider()

    portfolio.buttons.set_button_bar()


if __name__ == "__main__":
    run()
