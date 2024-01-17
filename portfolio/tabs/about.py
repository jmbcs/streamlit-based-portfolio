import streamlit as st
from settings import config
from streamlit_lottie import st_lottie


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """   
                # About Me 

                - Hi there! 👋 
                - My name is Júlio Silva and I am a 27-year-old developer from Portugal 🇵🇹
               

                ## Personal Details 

                - **Age:** 27
                - **Nationality:** Portuguese 🇵🇹
                - **Education:** M.Sc Electronics and Telecommunications Engineering, [University of Aveiro]
                - **Current Position** : Research & Development Engineer at Wavecom Technologies
                
                ## Hobbies & Interests

                When I'm not immersed in the world of coding, you can find me exploring various hobbies:

                - 😄 **Comedy:** Ricky Gervais, Daniel Sloss and Anthony Jeselnik fan right here
                - 📖 **Reading:** I feel that reading is essential to keep my mind sharp
                - 🎮 **Videogames:** Gaming is not just a hobby; it's a passion for me
                - 🍿 **Movies & Series:** I really love a binge watch session
                - 🏞️ **Hiking:** I fell that hiking is my way of connecting with nature
                - 💻 **Coding:** I love bringing ideas to life through code
                - 💪 **Gym:** Keeping both my mind and body in shape is crucial for my happiness
                - 🎵 **Music:** A playlist for every mood; music is my constant companion
                - 🌇 **Travelling:** I love travelling to new countries and visiting new cities
                - 💵 **Finances & Investing:** I enjoy keeping up with financial markets and exploring investment opportunities

                """
            )

        with col2:
            st_lottie(config.animations.about, height=800, width=700)
