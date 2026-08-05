import streamlit as st
import pandas as pd

from utils.api_client import api


def show():

    st.title("📚 Claim History")

    claims = api.get_claims()

    if not claims:

        st.warning("No claims found.")

        return

    df = pd.DataFrame(claims)

    # -----------------------------
    # Display Claims Table
    # -----------------------------

    st.subheader("All Claims")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # -----------------------------
    # Select Claim
    # -----------------------------

    claim_ids = df["claim_id"].tolist()

    selected_claim = st.selectbox(

        "Select Claim",

        claim_ids,

    )

    if st.button("View Details"):

        details = api.get_claim_details(
            selected_claim
        )

        if details is None:

            st.error("Unable to fetch claim.")

            return

        st.divider()

        st.subheader("Claim Details")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Claim ID",
                details["claim_id"],
            )

            st.metric(
                "Customer",
                details["customer_id"],
            )

            st.metric(
                "Policy",
                details["policy_number"],
            )

            st.metric(
                "Status",
                details["claim_status"],
            )

        with col2:

            st.metric(
                "Decision",
                details["final_decision"],
            )

            st.metric(
                "Claim Amount",
                f"₹ {details['claim_amount']:,.2f}",
            )

            st.metric(
                "Repair Cost",
                f"₹ {details['estimated_repair_cost']:,.2f}",
            )

            st.metric(
                "Damage Type",
                details["damage_type"],
            )

        st.divider()

        st.subheader("Accident Description")

        st.info(
            details["accident_description"]
        )

        st.divider()

        st.subheader("Processing Status")

        status_df = pd.DataFrame(
            [
                {
                    "CV": details["cv_status"],
                    "NLP": details["nlp_status"],
                    "RAG": details["rag_status"],
                }
            ]
        )

        st.dataframe(
            status_df,
            use_container_width=True,
            hide_index=True,
        )