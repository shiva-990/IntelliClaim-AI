import streamlit as st

from components.sidebar import show_sidebar

from dashboard import show_dashboard
from upload_claim import show as show_upload
from ai_analysis import show as show_ai
from crew_report import show as show_report
from claim_history import show as show_history


st.set_page_config(
    page_title="IntelliClaim AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

selected = show_sidebar()

if selected == "Dashboard":
    show_dashboard()

elif selected == "Upload Claim":
    show_upload()

elif selected == "AI Analysis":
    show_ai()

elif selected == "CrewAI Report":
    show_report()

elif selected == "Claim History":
    show_history()