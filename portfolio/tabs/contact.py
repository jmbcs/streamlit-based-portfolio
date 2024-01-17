import streamlit as st
from settings import config
from streamlit_lottie import st_lottie

import portfolio.style


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            # empty space
            st.markdown("#")

            st.markdown(
                f'<h2 style="margin-left: 215px">📮 Get In Touch With Me!</h2>',
                unsafe_allow_html=True,
            )

            contact_form = """
            <form action="https://formsubmit.co/julio.m.b.c.silva@gmail.com" method="POST" style="margin-left: 215px;">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name (Required)" required>
                <input type="email" name="email" placeholder="Your email (Required)" required>
                <input type="text" name="company" placeholder="Company (Required)" required >
                <textarea name="message" placeholder="Your message here"></textarea>
                <button type="submit">Send</button>
            </form>
            """

            st.markdown(contact_form, unsafe_allow_html=True)

            portfolio.style.set_style(path_to_style=config.styles.form)
        with col2:
            st_lottie(config.animations.contact, height=550, width=780)
    # add empty space (fixs jumping around between buttons)
    st.markdown("#\n" * 7)
