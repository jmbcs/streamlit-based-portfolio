import base64

import streamlit as st
from settings import config


def __get_pdf_display():
    with open(config.curriculum_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="75%" height=1080 type="application/pdf" style="margin-left: 11.5vw; margin-right: 11.5vw;">'
    return pdf_display


pdf_display = __get_pdf_display()


def set_section():
    st.markdown(pdf_display, unsafe_allow_html=True)


# # Add a Streamlit sidebar to dynamically adjust the PDF width
# pdf_width = st.sidebar.slider("PDF Width (%)", min_value=30, max_value=100, value=70)
# pdf_margin = (100 - pdf_width) / 2

# # Update the styling dynamically based on the selected PDF width
# st.markdown(f'<style>#pdfViewer {{ width: {pdf_width}%; margin-left: {pdf_margin}vw; margin-right: {pdf_margin}vw; }}</style>', unsafe_allow_html=True)
