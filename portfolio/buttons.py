import streamlit as st
from streamlit_option_menu import option_menu

import portfolio.tabs.about
import portfolio.tabs.contact
import portfolio.tabs.curriculum
import portfolio.tabs.experience
import portfolio.tabs.projects
import portfolio.tabs.skills


def set_button_bar():
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=[
                "About",
                "Work Experience",
                "Technical Skills",
                "Projects & Papers",
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
        )

        if selected == "About":
            portfolio.tabs.about.set_section()

        if selected == "Projects & Papers":
            portfolio.tabs.projects.set_section()

        if selected == "Contact":
            portfolio.tabs.contact.set_section()

        if selected == "Work Experience":
            portfolio.tabs.experience.set_section()

        if selected == "Technical Skills":
            portfolio.tabs.skills.set_section()

        if selected == "Curriculum":
            portfolio.tabs.curriculum.set_section()


def set_social_icons():
    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": [
            "https://www.linkedin.com/in/julio-miguel-silva/",
            "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        ],
        "GitHub": [
            "https://github.com/jmbcs",
            "https://static-00.iconduck.com/assets.00/github-icon-512x497-oppthre2.png",
        ],
    }

    social_icons_html = [
        f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 15px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' style='width: 25px; height: 25px;'></a>"
        for platform in social_icons_data
    ]

    st.write(
        f"""
    <div style="display: flex; justify-content: center; margin-bottom: 0px;">
        {''.join(social_icons_html)}
    </div>""",
        unsafe_allow_html=True,
    )


def set_tech_stack_icons():
    # Tech Stack Icons
    tech_stack_icons_data = {
        "Python": "https://img.icons8.com/color/96/000000/python.png",
        "Grafana": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Grafana_icon.svg",
        "Prometheus": "https://static-00.iconduck.com/assets.00/prometheus-icon-2047x2048-b3aicxlu.png",
        "Docker": "https://www.svgrepo.com/download/331370/docker.svg",
        "GitHub": "https://static-00.iconduck.com/assets.00/github-icon-512x497-oppthre2.png",
        "PostgreSQL": "https://cdn-icons-png.flaticon.com/512/5968/5968342.png",
    }

    tech_stack_icons_html = [
        f"<img class='tech-stack-icon' src='{tech_stack_icons_data[tech]}' alt='{tech}' style='width: 40px; height: 40px; margin-left: 15px ; margin-right: 15px;'>"
        for tech in tech_stack_icons_data
    ]

    st.write(
        f"""
    <div style="display: flex; justify-content: center; margin-bottom: 0px; ">
        {''.join(tech_stack_icons_html)}
    </div>""",
        unsafe_allow_html=True,
    )
