import os
import sys

# required to deploy app in streamlit
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import hydralit as hy

# when we import hydralit, we automatically get all of Streamlit
import hydralit as hy
import streamlit as st

import portfolio.buttons
import portfolio.image
import portfolio.sections
import portfolio.style
from portfolio.settings import config

over_theme = {
    "txc_inactive": "#777777",
    "txc_active": "#ff4c4c",
    "menu_background": "transparent",
}
app = hy.HydraApp(
    title="",
    favicon="🐙",
    hide_streamlit_markers=True,
    banner_spacing=[5, 30, 60, 30, 5],
    use_navbar=True,
    navbar_sticky=False,
    navbar_animation=True,
    layout="wide",
    navbar_theme=over_theme,
)


@app.addapp(title="About Me")
def section_about_me():
    # hy.info("Hello from app 1")
    portfolio.sections.set_about_section()


@app.addapp(title="Work Experience")
def section_work_experience():
    portfolio.sections.set_experience_section()


@app.addapp(title="Skills")
def section_skills():
    portfolio.sections.set_skills_section()


@app.addapp(title="Projects")
def section_projects():
    portfolio.sections.set_projects_section()


@app.addapp(title="Curriculum")
def section_curriculum():
    portfolio.sections.set_curriculum_section()


@app.addapp(title="Contact Me")
def section_contact():
    portfolio.sections.set_contact_section()


def run():
    # Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
    # app.run()

    # hy.set_page_config(
    #     page_title="Portfolio - Júlio Silva",
    #     page_icon="💼",
    #     layout="wide",
    #     initial_sidebar_state="collapsed",
    # )

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

    # add tech bar
    st.markdown(config.html.structure_tech_stack, unsafe_allow_html=True)

    app.run()

    # add button bar and logic for tabs
    # portfolio.buttons.set_main_button_bar()

    # # add divider at end
    st.markdown(config.html.structure_divider, unsafe_allow_html=True)

    # # add footer with link to github code
    st.markdown(config.html.structure_footer, unsafe_allow_html=True)


if __name__ == "__main__":
    run()
