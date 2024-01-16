import base64

import streamlit as st

st.set_page_config(page_title="Júlio Silva's Porfolio", page_icon="💻")

# CSS styles file
with open("styles/main.css") as f:
    st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Profile image file
with open("docs/profile.jpg", "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# PDF CV file
with open("docs/cv_julio_silva.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

    # Top title
    st.write(
        f"""<div class="title"><strong>Hi! My name is</strong> Júlio Silva 👋</div>""",
        unsafe_allow_html=True,
    )


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

# Subtitle
st.write(
    f"""<div class="subtitle" style="text-align: center;">Software Engineer</div>""",
    unsafe_allow_html=True,
)

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

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    st.download_button(
        label="📕 Check my CV",
        data=pdf_bytes,
        file_name="julio_silva.pdf",
        mime="application/pdf",
    )
