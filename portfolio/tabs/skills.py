import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.buttons


def __insert_skill(skill_type: str, skills: str):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            f"<div style='margin-left: 11vw; font-size: 14px; line-height: 2.5; white-space: nowrap;'><strong>{skill_type}</strong> </div>",
            unsafe_allow_html=True,
        )

    with col2:
        split_skills = [skill.strip() for skill in skills.split(",")]

        skill_snippets = " ".join(
            [
                f"<code style='color: #ff4c4c; font-size: 14px; line-height: 2.5'>{skill}</code>"
                if (i + 1) % 3 != 0
                else f"<code style='color: #ff4c4c; font-size: 14px; line-height: 2.5;'>{skill}</code><br>"
                for i, skill in enumerate(split_skills)
            ]
        )

        st.markdown(
            f"<div style='margin-left: 11vw;'>{skill_snippets}</div>",
            unsafe_allow_html=True,
        )

    # add small space
    st.markdown("#\n")


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <h2 style='margin-left: 11vw;'>Tech Stack</h2>
                """,
                unsafe_allow_html=True,
            )

            portfolio.buttons.set_tech_stack_icons()

            st.markdown(
                """
                <h2 style='margin-left: 11vw;'>Tech Skills</h2>
                """,
                unsafe_allow_html=True,
            )
            __insert_skill("Programming", "Python, Golang, Bash")
            __insert_skill(
                "Databases",
                "SQL, NoSQL, PostegreSQL, Victoriametrics, Promscale, Prometheus, Elasticsearch, PromQL, pgAdmin",
            )
            __insert_skill("Dashboading", "Grafana, Kibana")
            __insert_skill("Containerization", "Docker, Docker Compose")
            __insert_skill("Data formats", "JSON, CSV, Protobuf, YAML")
            __insert_skill("Others", "Git, Telegraf, Linux, direnv, Makefile")

            st.markdown(
                """
                <h2 style='margin-left: 11vw;'> Python Skills</h2>
                """,
                unsafe_allow_html=True,
            )

            __insert_skill(
                "Software Development",
                "FastAPI, SQLAlchemy, Aiohttp, Pydantic, Requests",
            )
            __insert_skill("Web Development", "Streamlit")
            __insert_skill("Data Analytics", "Pandas, Numpy, Matplotlib, Tensorflow")
            __insert_skill("Computer Vision", "ImageAI, OpenCV, Ultralytics")

        with col2:
            st_lottie(config.animations.skills)
