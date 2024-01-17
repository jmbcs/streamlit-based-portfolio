import streamlit as st
from settings import config

import portfolio.buttons
import portfolio.image
import portfolio.style


def run():
    st.set_page_config(
        page_title="Porfolio - Júlio Silva", page_icon="💼", layout="wide"
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
        f"""<div class="subtitle" style="text-align: center;color: #ff4c4c;">Backend Developer <span style="color: #ffffff;">- </span>Data Analyst</div>""",
        unsafe_allow_html=True,
    )

    portfolio.buttons.set_social_icons()

    # Displaying Markdown with icons

    divider_html = '<div style="margin-left: 215px; margin-right: 215px; margin-top: 20px; margin-bottom: 20px; border-top: 2px solid #888;"></div>'
    st.markdown(divider_html, unsafe_allow_html=True)

    portfolio.buttons.set_button_bar()

    st.markdown(divider_html, unsafe_allow_html=True)

    text_html = "<div style='text-align: center; color: #ffffff;'>If you liked my portfolio, feel free to check my code at :</div>"

    st.markdown(text_html, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
