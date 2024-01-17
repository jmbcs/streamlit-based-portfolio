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
                    <li> My name is Júlio Silva and I am a 27-year-old developer from Portugal 🇵🇹</li>
                </ul>
                

                <h2> Personal Details</h2>

                <ul>
                    <li><strong>Age:</strong> 27</li>
                    <li><strong>Nationality:</strong> Portuguese 🇵🇹</li>
                    <li><strong>Current Position:</strong> Research & Development Engineer at Wavecom Technologies</li>
                    <li><strong>Work Experience:</strong> 3 years</li>
                    <li><strong>Education:</strong> M.Sc Electronics and Telecommunications Engineering, <br>University of Aveiro</a></li>
                </ul>

                <h2>Hobbies & Interests</h2>

          

                <ul>
                    <li>😄 <strong>Comedy:</strong> Ricky Gervais, Daniel Sloss, and Anthony Jeselnik fan right here</li>
                    <li>📖 <strong>Reading:</strong> I feel that reading is essential to keep my mind sharp</li>
                    <li>🎮 <strong>Videogames:</strong> Gaming is not just a hobby; it's a passion for me</li>
                    <li>🍿 <strong>Movies & Series:</strong> I really love a binge-watch session</li>
                    <li>🏞️ <strong>Hiking:</strong> I feel that hiking is my way of connecting with nature</li>
                    <li>💻 <strong>Coding:</strong> I love bringing ideas to life through code</li>
                    <li>💪 <strong>Gym:</strong> Keeping both my mind and body in shape is crucial for my happiness</li>
                    <li>🎵 <strong>Music:</strong> A playlist for every mood; music is my constant companion</li>
                    <li>🌇 <strong>Travelling:</strong> I love traveling to new countries and visiting new cities</li>
                    <li>💵 <strong>Finances & Investing:</strong> I enjoy keeping up with financial markets and exploring investment
                    opportunities</li>
                </ul>

                </body>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st_lottie(config.animations.about, height=800, width=700)
