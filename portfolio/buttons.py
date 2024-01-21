import streamlit as st
from streamlit_option_menu import option_menu

import portfolio.sections


def set_main_button_bar():
    with st.container():
        selected = option_menu(
            key="main_menu",
            menu_title=None,
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
            orientation="horizontal",
            styles={
                "icon": {"color": "white"},
                "container": {
                    "width": "75%",
                    "padding": "0!important",
                    "white-space": "nowrap",
                },
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "center",
                    "--hover-color": "#383838",
                    "white-space": "nowrap",  # Prevent text wrapping
                },
                "nav-link-selected": {"background-color": "#ff4c4c"},
            },
        )

        if selected == "About":
            portfolio.sections.set_about_section()

        if selected == "Work":
            portfolio.sections.set_experience_section()

        if selected == "Projects":
            set_projects_button_bar()

        if selected == "Contact":
            portfolio.sections.set_contact_section()

        if selected == "Skills":
            portfolio.sections.set_skilsl_section()

        if selected == "Curriculum":
            portfolio.sections.set_curriculum_section()


def set_projects_button_bar():
    with st.container():
        selected = option_menu(
            key="project_menu",
            menu_title=None,
            options=["BigHPC", "Portfolio", "Thesis"],
            icons=[
                "code-slash",
                "code-slash",
                "code-slash",
            ],
            orientation="horizontal",
            styles={
                "icon": {"color": "white"},
                "container": {
                    "width": "25%",
                    "height": "25%",
                    "padding": "0!important",
                    "white-space": "nowrap",  # Prevent text wrapping
                },
                "nav-link": {
                    "font-size": "10px",
                    "text-align": "center",
                    "--hover-color": "#383838",
                    "white-space": "nowrap",  # Prevent text wrapping
                },
                "nav-link-selected": {"background-color": "#e06363"},
            },
        )

        if selected == "Thesis":
            portfolio.sections.set_projects_section(project="THESIS")

        if selected == "BigHPC":
            portfolio.sections.set_projects_section(project="BIGHPC")

        if selected == "Portfolio":
            portfolio.sections.set_projects_section(project="PORTFOLIO")
