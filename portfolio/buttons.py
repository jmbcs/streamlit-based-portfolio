import streamlit as st
from streamlit_option_menu import option_menu

import portfolio.sections


def set_main_button_bar():
    with st.sidebar:
        with st.container():
            selected = option_menu(
                menu_title="Menu",
                menu_icon="cast",
                key="main_menu",
                options=[
                    "About",
                    "Work",
                    "Skills",
                    "Projects",
                    "Curriculum",
                    "Contact",
                ],
                icons=[
                    "person",
                    "briefcase",
                    "wrench",
                    "code-slash",
                    "book",
                    "chat-left-text-fill",
                ],
                orientation="vertical",
                styles={
                    "icon": {"color": "white"},
                    "container": {
                        "padding": "10px",
                        "white-space": "nowrap",
                        "font-color": "#000000",
                    },
                    "nav-link": {
                        "font-size": "20px",
                        "text-align": "left",
                        "--hover-color": "#383838",
                        "white-space": "nowrap",  # Prevent text wrapping
                        "font-color": "#000000",
                    },
                    "nav-link-selected": {"background-color": "#ff4c4c"},
                },
            )

    if selected == "About":
        portfolio.sections.set_about_section()

    if selected == "Work":
        portfolio.sections.set_experience_section()

    if selected == "Projects":
        portfolio.sections.set_projects_section()

    if selected == "Contact":
        portfolio.sections.set_contact_section()

    if selected == "Skills":
        portfolio.sections.set_skilsl_section()

    if selected == "Curriculum":
        portfolio.sections.set_curriculum_section()
