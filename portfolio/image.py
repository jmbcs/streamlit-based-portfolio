import base64

import streamlit as st
from settings import config


def set_profile_image():
    # Profile image file
    with open(config.profile_image_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # Profile image
    st.write(
        f"""
        <div class="container">
            <div class="box">
                <div class="spin-container">
                    <div class="shape">
                        <div class="bd">
                            <img src="{img}" alt="Enric Domingo">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
