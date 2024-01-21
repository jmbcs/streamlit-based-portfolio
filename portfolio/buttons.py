import streamlit as st
from streamlit_option_menu import option_menu

import portfolio.tabs.about
import portfolio.tabs.contact
import portfolio.tabs.curriculum
import portfolio.tabs.experience
import portfolio.tabs.projects
import portfolio.tabs.skills
from portfolio.settings import config


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
                "container": {"width": "75%", "padding": "0!important"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "center",
                    "--hover-color": "#383838",
                },
                "nav-link-selected": {"background-color": "#ff4c4c"},
            },
        )

        if selected == "About":
            portfolio.tabs.about.set_section()

        if selected == "Work":
            portfolio.tabs.experience.set_section()

        if selected == "Projects":
            set_projects_button_bar()

        if selected == "Contact":
            portfolio.tabs.contact.set_section()

        if selected == "Skills":
            portfolio.tabs.skills.set_section()

        if selected == "Curriculum":
            portfolio.tabs.curriculum.set_section()


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
                },
                "nav-link": {
                    "font-size": "10px",
                    "text-align": "center",
                    "--hover-color": "#383838",
                },
                "nav-link-selected": {"background-color": "#e06363"},
            },
        )

        if selected == "Thesis":
            portfolio.tabs.projects.set_thesis_section()

        if selected == "BigHPC":
            portfolio.tabs.projects.set_bighpc_section()

        if selected == "Portfolio":
            portfolio.tabs.projects.set_portfolio_section()
