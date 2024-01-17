import streamlit as st
from settings import config
from streamlit_lottie import st_lottie


def set_section():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            # Convert content to HTML and apply styling to shift text 215px to the right
            st.markdown(
                """
                <div style="margin-left: 215px;font-size: 14px;">
                    <h2>Work History</h2>
                    <p>💼 <strong>Position</strong> : Research and Development Engineer</strong></p>
                    <p>🏢 <strong>Company</strong> : <a href="https://www.wavecom.com" target="_blank" style="color: #ff4c4c; font-weight: bold;">Wavecom Technologies</a></p>
                    <p>📅 <strong>Date</strong> : 01/2021 - Present</p>
                    <ul>
                        <li>► Decision-making in diverse projects from inception to production.</li>
                        <li>► Designed and implemented <strong style="color: #ff4c4c;">ETL pipelines</strong>.</li>
                        <li>► Developed microservices both in <strong style="color: #ff4c4c;">python</strong> and <strong style="color: #ff4c4c;">golang</strong></li>
                        <li>► Developed scripts and automated processes using both <strong style="color: #ff4c4c;">python</strong> and <strong style="color: #ff4c4c;">Shell</strong> for efficient workflow management.</li>
                        <li>► Created <strong style="color: #ff4c4c;">APIs</strong> for <strong style="color: #ff4c4c;">SQL</strong> and <strong style="color: #ff4c4c;">NoSQL</strong> databases.</li>
                        <li>► Managed databases such as <strong style="color: #ff4c4c;">PostgreSQL</strong>, <strong style="color: #ff4c4c;">Victoriametrics</strong>.</li>
                        <li>► Implemented <strong style="color: #ff4c4c;">Protocol Buffers</strong> and <strong style="color: #ff4c4c;">gRPC</strong> for efficient microservices communication.</li>
                        <li>► Developed <strong style="color: #ff4c4c;">Docker images</strong>, orchestrated applications with <strong style="color: #ff4c4c;">Docker Compose</strong>.</li>
                        <li>► Employed <strong style="color: #ff4c4c;">Telegraf</strong> to optimize the efficiency of data collection, processing and seamless transfer to databases.</li>
                        <li>► Utilized <strong style="color: #ff4c4c;">Version Control</strong> Systems for code integrity.</li>
                        <li>► Designed comprehensive <strong style="color: #ff4c4c;">Grafana</strong> dashboards for effective data visualization.</li>
                        <li>► Applied <strong style="color: #ff4c4c;">Computer Vision</strong> algorithms and utilized ONVIF protocol.</li>
                        <li>► Experience with <strong style="color: #ff4c4c;">HPC</strong> systems (developed a monitoring framework with alarms). </li>
                        <li>► Collaborated with global partners. </li>
                        <li>► Conducted client meetings, ensuring requirements fulfillment. </li>
                    </ul>
                </div>

                """,
                unsafe_allow_html=True,
            )
        with col2:
            st_lottie(config.animations.experience, height=600, width=700)
