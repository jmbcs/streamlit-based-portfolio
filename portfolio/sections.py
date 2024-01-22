import base64

import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.style


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


def set_contact_section():
    with st.container():
        st.markdown(config.html.section_contact, unsafe_allow_html=True)

        portfolio.style.set_style(path_to_style=config.styles.form)


def set_curriculum_section():
    st.markdown(config.html.section_curriculum, unsafe_allow_html=True)


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


def set_skills_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                config.html.section_skills,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.skills, quality="high")


def set_projects_section():
    with st.expander("Project - BigHPC"):
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(config.html.section_project_bighpc, unsafe_allow_html=True)

            with col2:
                st.markdown(config.html.project_bighpc_video, unsafe_allow_html=True)
    with st.expander("Project - Thesis"):
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(config.html.section_project_thesis, unsafe_allow_html=True)
            with col2:
                st_lottie(config.animations.computer, quality="high")
    with st.expander("Project - Porfolio"):
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    config.html.section_project_portfolio,
                    unsafe_allow_html=True,
                )

            with col2:
                st_lottie(config.animations.computer, quality="high")
