import streamlit as st


def show_header():

    col1, col2 = st.columns([6, 1])

    with col1:

        st.title("🚗 IntelliClaim AI Powered Insurance Claim Processing Platform Version 1.0")

        st.caption(
            "AI Powered Insurance Claim Processing System"
        )

    with col2:

        st.metric(
            "Status",
            "🟢 Online"
        )