from pathlib import Path

import streamlit as st

import portfolio.buttons as buttons
import portfolio.image as image
import portfolio.style as style

# with st.echo():

PATH_TO_STYLE = Path("styles/main.css")


st.set_page_config(page_title="Júlio Silva's Porfolio", page_icon="💻", layout="wide")


style.set_style(path_to_style=PATH_TO_STYLE)


image.set_profile_image()

# Top title
st.write(
    f"""<div class="title"><strong>Hi! My name is</strong> Júlio Silva 👋</div>""",
    unsafe_allow_html=True,
)


# Subtitle
st.write(
    f"""<div class="subtitle" style="text-align: center;">Backend Engineer</div>""",
    unsafe_allow_html=True,
)


buttons.set_social_icons()
buttons.set_button_bar()
buttons.set_pdf_button()
