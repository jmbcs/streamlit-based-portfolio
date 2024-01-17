import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


def get_lottie_animation(url: str) -> bytes | None:
    response = requests.get(url)
    if response.status_code != 200:
        data = None
    else:
        data = response.json()
    return data


COMPUTER_ANIMATION = get_lottie_animation(
    url="https://lottie.host/b3725bf1-207f-47b0-8f42-f9b2fbde17f5/AICc3sX4ge.json"
)

ABOUT_ANIMATION = get_lottie_animation(
    url="https://lottie.host/0898ab9f-2597-4fa5-95e5-bce8b5ad3002/SRb1DCS2Vg.json"
)

CONTACT_ANIMATION = get_lottie_animation(
    url="https://lottie.host/556f0732-5b1f-4e8c-8f65-c1e86e73ca8f/mOJPjTHpMU.json"
)

# EXPERIENCE_ANIMATION = get_lottie_animation(
#     url="https://lottie.host/1ebbb2c4-1379-49c9-a9e0-7ae421f7baf1/nfUWf4lmzR.json"
# )
EXPERIENCE_ANIMATION = get_lottie_animation(
    url="https://lottie.host/98bae704-fc8c-4869-b698-820a1bfebb64/sY8eoRSEyZ.json"
)


def set_pdf_button():
    col1, col2, col3 = st.columns([1, 1, 1])

    # PDF CV file
    with open("docs/cv_julio_silva.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    with col1:
        st.download_button(
            label="📕 Check my CV",
            data=pdf_bytes,
            file_name="julio_silva.pdf",
            mime="application/pdf",
        )


def set_button_bar():
    st.write("----------------")
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["About", "Projects", "Contact", "Experience"],
            icons=["person", "code-slash", "chat-left-text-fill", "briefcase"],
            orientation="horizontal",
        )

        if selected == "About":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("27 Year old")
                    st.subheader("🇵🇹 Portuguese")

                    st.write("------")
                    st.subheader("Hobbies")

                    st.code(
                        body=""" 
                           
                            \n      📖 Reading
                            \n      🎮 Videogames
                            \n      💻 Coding 
                            \n      💪 Gym
                            \n      🎵 Music 
                            \n      🌇 Travelling
                            \n      💵 Finances & Investing
                            """
                    )

                with col2:
                    if ABOUT_ANIMATION != None:
                        st_lottie(ABOUT_ANIMATION, height=700, width=900)

        if selected == "Projects":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("...")
                with col2:
                    if COMPUTER_ANIMATION != None:
                        st_lottie(COMPUTER_ANIMATION, height=700, width=900)
        if selected == "Contact":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("...")
                with col2:
                    if CONTACT_ANIMATION != None:
                        st_lottie(CONTACT_ANIMATION, height=700, width=900)

        if selected == "Experience":
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Research and Development Engineer")
                    st.text_area("uasghduisagduisa")

                    # st.write("------")
                    # st.subheader("Hobbies")

                    # st.code(
                    #     body="""

                    #         \n      📖 Reading
                    #         \n      🎮 Videogames
                    #         \n
                    #         \n      💪 Gym
                    #         \n
                    #         \n      🌇 Travelling
                    #         \n      💵 Finances & Investing
                    #         """
                    # )
                with col2:
                    if EXPERIENCE_ANIMATION != None:
                        st_lottie(EXPERIENCE_ANIMATION, height=700, width=900)

    st.write("----------------")


def set_social_icons():
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
