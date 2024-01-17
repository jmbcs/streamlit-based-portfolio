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
                "Projects",
                "Contact",
                "Work Experience",
                "Technical Skills",
                "Curriculum",
            ],
            icons=[
                "person",
                "code-slash",
                "chat-left-text-fill",
                "briefcase",
                "wrench",
                "book",
            ],
            orientation="horizontal",
        )

        if selected == "About":
            portfolio.tabs.about.set_section()

        if selected == "Projects":
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
            "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg",
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
