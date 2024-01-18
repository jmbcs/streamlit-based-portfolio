import streamlit as st
import streamlit.components.v1 as components
from settings import config
from streamlit_lottie import st_lottie

import portfolio.buttons

# def set_section():
#     # portfolio.buttons.set_button_bar()
#     with st.container():
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown(config.html.project_bighpc, unsafe_allow_html=True)

#             # st.markdown(config.html.project_thesis, unsafe_allow_html=True)
#             # st.markdown(config.html.project_portfolio, unsafe_allow_html=True)

#         with col2:
#             # st_lottie(config.animations.computer, quality="high")
#             # st.video(
#             #     "https://www.youtube.com/watch?v=5gaiovo9DD0",
#             #     format="video/mp4",
#             #     start_time=0,
#             # )
#             st.markdown(config.html.project_bighpc_video, unsafe_allow_html=True)


def set_bighpc_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(config.html.project_bighpc, unsafe_allow_html=True)

        with col2:
            # st_lottie(config.animations.computer, quality="high")
            st.markdown(config.html.project_bighpc_video, unsafe_allow_html=True)


def set_thesis_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(config.html.project_thesis, unsafe_allow_html=True)
        with col2:
            st_lottie(config.animations.computer, quality="high")


def set_portfolio_section():
    # portfolio.buttons.set_projects_button_bar()
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(config.html.project_portfolio, unsafe_allow_html=True)

        with col2:
            st_lottie(config.animations.computer, quality="high")

            # st.markdown(config.html.project_bighpc_video, unsafe_allow_html=True)
