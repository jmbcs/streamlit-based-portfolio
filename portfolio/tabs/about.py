import streamlit as st
from settings import config
from streamlit_lottie import st_lottie


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <head>
                <style>
                    h2 {
                    margin-left: 215px;
                    }
                    ul {
                    margin-left: 200px;
                    padding-left: 0px; /* Adjusted padding for better alignment of list items */
                }
                </style>
                </head>

                <body>

                <h2> About Me </h2>
                <ul>
                    <li> Hi there! 👋</li>
                    <li> My name is Júlio Silva and I am a developer from Portugal 🇵🇹</li>
                </ul>
                

                <h2> Personal Details</h2>

                <ul>
                    <li><strong style="color: #ff4c4c;">Age</strong> 27</li>
                    <li><strong style="color: #ff4c4c;">Nationality</strong> Portuguese</li>
                    <li><strong style="color: #ff4c4c;">Current Position</strong> Research & Development Engineer at Wavecom Technologies</li>
                    <li><strong style="color: #ff4c4c;">Work Experience</strong> 3 years</li>
                    <li><strong style="color: #ff4c4c;">Education</strong> M.Sc Electronics and Telecommunications Engineering, <br>University of Aveiro</a></li>
                </ul>

                <h2>Hobbies & Interests</h2>

          

                <ul>
                    <li>😄 <strong style="color: #ff4c4c;">Comedy</strong> Ricky Gervais, Daniel Sloss, and Anthony Jeselnik fan right here</li>
                    <li>📖 <strong style="color: #ff4c4c;">Reading</strong> Reading is essential to keep my mind sharp</li>
                    <li>🎮 <strong style="color: #ff4c4c;">Videogames</strong> I am a certified gamer since 6 years old</li>
                    <li>🍿 <strong style="color: #ff4c4c;">Movies & Series</strong> You know nothing Jon Snow!</li>
                    <li>🏞️ <strong style="color: #ff4c4c;">Hiking</strong> Hiking with the family is a time well spent</li>
                    <li>💻 <strong style="color: #ff4c4c;">Coding</strong> I love bringing ideas to life through code</li>
                    <li>💪 <strong style="color: #ff4c4c;">Gym</strong> Keeping both my mind and body in shape is crucial for my happiness</li>
                    <li>🎵 <strong style="color: #ff4c4c;">Music</strong> Music is a constant companion in my life</li>
                    <li>🌇 <strong style="color: #ff4c4c;">Travelling</strong> I love visiting new countries and cities</li>
                    <li>💵 <strong style="color: #ff4c4c;">Finances & Investing</strong> I like to keep up with financial markets and exploring new investment opportunities</li>
                </ul>

                </body>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.about, height=700, width=800)
