import base64

import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.style


def __get_pdf_display() -> str:
    url_link = (
        "https://github.com/jmbcs/portfolio/blob/main/portfolio/docs/cv_julio_silva.pdf"
    )
    with open(config.curriculum_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""<object data="data:application/pdf;base64, {base64_pdf}" type="application/pdf" width="75%" height="1080" style="margin-left: auto; margin-right: auto; display: block;">
        <p style="text-align: center;">Your browser does not support embedded PDF files. You can download my curriculum <a href="{url_link}" style="color: #ff4c4c;" target="_blank">here</a> instead.</p>
    </object>"""

    return pdf_display


pdf_display = __get_pdf_display()


def set_about_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                config.html.section_about,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.about, quality="high")


def set_contact_ection():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(config.html.section_contact, unsafe_allow_html=True)

            portfolio.style.set_style(path_to_style=config.styles.form)
        with col2:
            st_lottie(config.animations.contact, quality="high", speed=2)


def set_curriculum_section():
    st.markdown(pdf_display, unsafe_allow_html=True)


def set_experience_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                config.html.section_experience,
                unsafe_allow_html=True,
            )
        with col2:
            st_lottie(config.animations.experience, quality="high")


def set_skilsl_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                config.html.section_skills,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.skills, quality="high")


def set_projects_section(project: str):
    if project == "BIGHPC":
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(config.html.section_project_bighpc, unsafe_allow_html=True)

            with col2:
                st.markdown(config.html.project_bighpc_video, unsafe_allow_html=True)
    if project == "THESIS":
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(config.html.section_project_thesis, unsafe_allow_html=True)
            with col2:
                st_lottie(config.animations.computer, quality="high")

    if project == "PORTFOLIO":
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    config.html.section_project_portfolio, unsafe_allow_html=True
                )

            with col2:
                st_lottie(config.animations.computer, quality="high")
