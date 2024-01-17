import base64

import streamlit as st
from settings import config


def __get_pdf_display():
    with open(config.curriculum_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    # Adding left and right margins to the PDF display
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="1320" height="1200" type="application/pdf" style="margin-left: 220px; margin-right: 215px;">'
    return pdf_display


pdf_display = __get_pdf_display()


def set_section():
    st.markdown(pdf_display, unsafe_allow_html=True)
