import streamlit as st
import pandas as pd

from utils.api_client import api


def show_recent_claims():

    claims = api.get_claims()

    if not claims:
        st.info("No claims found.")
        return

    df = pd.DataFrame(claims)

    df = df[
        [
            "claim_id",
            "customer_id",
            "policy_number",
            "claim_status",
            "final_decision",
        ]
    ]

    df.columns = [
        "Claim ID",
        "Customer",
        "Policy",
        "Status",
        "Decision",
    ]

    st.subheader("📋 Recent Claims")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )