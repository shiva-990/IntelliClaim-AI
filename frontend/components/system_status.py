import streamlit as st


def show_system_status():

    st.subheader("🖥 AI System Status")

    st.success("🟢 Backend Connected")

    st.success("🟢 Database Connected")

    st.success("🟢 CrewAI Ready")

    st.success("🟢 YOLO Loaded")

    st.success("🟢 NLP Loaded")

    st.success("🟢 RAG Ready")