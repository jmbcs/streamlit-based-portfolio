import base64
import json

import streamlit as st


def set_profile_image():
    # Profile image file
    with open("docs/profile.jpg", "rb") as img_file:
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
