import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import portfolio.button_pages.about
import json


# with open("portfolio/animation/about.json") as source:
#     ABOUT_ANIMATION = json.load(source)

with open("portfolio/animation/computer.json") as source:
    COMPUTER_ANIMATION = json.load(source)

with open("portfolio/animation/contact.json") as source:
    CONTACT_ANIMATION = json.load(source)

with open("portfolio/animation/experience.json") as source:
    EXPERIENCE_ANIMATION = json.load(source)

with open("portfolio/animation/skills.json") as source:
    SKILLS_ANIMATION = json.load(source)


def set_pdf_button():
    col1, col2, col3 = st.columns([1, 1, 1])

    # PDF CV file
    with open("docs/cv_julio_silva.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    with col1:
        st.download_button(
            label="📕 Check my CV",
            data=pdf_bytes,
            file_name="julio_silva.pdf",
            mime="application/pdf",
        )


def set_button_bar():
    st.write("----------------")
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
            portfolio.button_pages.about.set_about_section()

        if selected == "Projects":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("...")
                with col2:
                    st_lottie(COMPUTER_ANIMATION, height=700, width=900)
        if selected == "Contact":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("...")
                with col2:
                    st_lottie(CONTACT_ANIMATION, height=700, width=900)

        if selected == "Work Experience":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Research and Development Engineer")

                with col2:
                    st_lottie(EXPERIENCE_ANIMATION, height=600, width=800)
        if selected == "Technical Skills":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Research and Development Engineer")

                with col2:
                    st_lottie(SKILLS_ANIMATION, height=600, width=800)

        if selected == "Curriculum":
            import base64

            def displayPDF(file="docs/cv_julio_silva.pdf"):
                # Opening file from file path
                with open(file, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")

                # Embedding PDF in HTML
                pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="1750" height="1300" type="application/pdf">'

                # Displaying File
                st.markdown(pdf_display, unsafe_allow_html=True)

            displayPDF()

    st.write("----------------")


def set_social_icons():
    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": [
            "https://github.com/jmbcs",
            "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        ],
        "GitHub": [
            "https://github.com/jmbcs",
            "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg",
        ],
    }

    social_icons_html = [
        f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>"
        for platform in social_icons_data
    ]

    st.write(
        f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""",
        unsafe_allow_html=True,
    )
