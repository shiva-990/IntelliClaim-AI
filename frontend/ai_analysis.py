import streamlit as st

from utils.api_client import api


def show():

    st.title("🤖 AI Analysis Dashboard")

    st.divider()

    claim_id = st.text_input(
        "Enter Claim ID"
    )

    if st.button(
        "Analyze Claim",
        use_container_width=True,
    ):

        if not claim_id.strip():

            st.warning(
                "Please enter a Claim ID."
            )

            return

        with st.spinner(
            "Loading AI Analysis..."
        ):

            report = api.get_report(
                claim_id
            )

        # -----------------------------
        # API Error
        # -----------------------------
        if "error" in report:

            st.error(report["error"])
            return

        st.success(
            "Analysis Loaded Successfully!"
        )

        st.divider()

        st.subheader("📋 Claim Information")

        st.write(
            f"**Claim ID:** {report.get('claim_id')}"
        )

        st.divider()

        # ==================================================
        # Computer Vision
        # ==================================================
        with st.expander(
            "🚗 Computer Vision",
            expanded=True,
        ):

            cv = report.get("cv")

            if not cv:

                st.info("No Computer Vision result found.")

            else:

                for index, item in enumerate(cv, start=1):

                    st.markdown(
                        f"### Image {index}"
                    )

                    st.write(
                        "Image:",
                        item.get("image_name")
                    )

                    st.write(
                        "Severity:",
                        item.get("severity")
                    )

                    st.write(
                        "Repair Cost:",
                        item.get("repair_cost")
                    )

                    st.write(
                        "Repair Days:",
                        item.get("repair_days")
                    )

                    st.write(
                        "Repairable:",
                        item.get("repairable")
                    )

                    st.subheader("Detected Objects")

                    detections = item.get(
                        "detections",
                        [],
                    )

                    if detections:

                        st.dataframe(
                            detections,
                            use_container_width=True,
                        )

                    else:

                        st.info(
                            "No detections found."
                        )

        # ==================================================
        # NLP
        # ==================================================
        with st.expander(
            "📝 NLP Analysis",
            expanded=True,
        ):

            nlp = report.get("nlp")

            if not nlp:

                st.info(
                    "No NLP analysis available."
                )

            else:

                st.write(
                    "Accident Type:",
                    nlp.get("accident_type")
                )

                st.write(
                    "Vehicle Part:",
                    nlp.get("vehicle_part")
                )

                st.write(
                    "Weather:",
                    nlp.get("weather")
                )

                st.write(
                    "Severity:",
                    nlp.get("severity")
                )

                st.write(
                    "Cause:",
                    nlp.get("cause")
                )

        # ==================================================
        # Decision
        # ==================================================
        with st.expander(
            "⚖️ Decision Engine",
            expanded=True,
        ):

            decision = report.get("decision")

            if not decision:

                st.info(
                    "No decision available."
                )

            else:

                st.metric(
                    "Decision",
                    decision.get("decision")
                )

                st.metric(
                    "Coverage",
                    decision.get("coverage")
                )

                st.metric(
                    "Fraud Score",
                    decision.get("fraud_score")
                )

                st.write(
                    "Reason"
                )

                st.info(
                    decision.get("reason")
                )