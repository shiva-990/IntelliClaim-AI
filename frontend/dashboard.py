import streamlit as st

from components.sidebar import show_sidebar
from components.header import show_header
from components.cards import show_cards
from components.charts import show_charts

from components.recent_claims import show_recent_claims
from components.system_status import show_system_status
from components.crew_report import show_crew_report
from components.vehicle_preview import show_vehicle_preview


def show_dashboard():

    show_header()

    show_cards()

    st.divider()

    show_charts()
    st.divider()

    left, right = st.columns([2, 1])

    with left:
       show_recent_claims()

    with right:
       show_system_status()

    st.divider()

    left, right = st.columns(2)

    with left:
       show_crew_report()

    with right:
       show_vehicle_preview()