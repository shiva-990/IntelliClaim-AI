import streamlit as st
from streamlit_option_menu import option_menu


def show_sidebar():

    with st.sidebar:

        st.title("🚗 IntelliClaim AI")

        selected = option_menu(
            menu_title="Navigation",
            options=[
                "Dashboard",
                "Upload Claim",
                "AI Analysis",
                "CrewAI Report",
                "Claim History",
            ],
            icons=[
                "speedometer2",
                "cloud-upload",
                "robot",
                "file-earmark-text",
                "clock-history",
            ],
            default_index=0,
        )

    return selected