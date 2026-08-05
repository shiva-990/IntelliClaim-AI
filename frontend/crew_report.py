import streamlit as st

from utils.api_client import api
from utils.pdf_generator import generate_pdf

def show():

    st.title("🤖 CrewAI Executive Report")

    st.divider()

    claim_id = st.text_input(
        "Claim ID",
        key="crew_claim",
    )

    if st.button(
        "Generate Report",
        use_container_width=True,
    ):

        if not claim_id.strip():

            st.warning(
                "Enter Claim ID"
            )

            return

        report = api.get_report(
            claim_id
        )

        if "error" in report:

            st.error(
                report["error"]
            )

            return

        st.success(
            "Executive Report Generated"
        )

        st.divider()

        st.subheader("📋 Claim")

        st.write(
            f"**Claim ID :** {report['claim_id']}"
        )

        decision = report.get("decision")

        if decision:

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Decision",
                decision["decision"],
            )

            c2.metric(
                "Coverage",
                decision["coverage"],
            )

            c3.metric(
                "Fraud Score",
                decision["fraud_score"],
            )

        st.divider()

        st.subheader("🚗 Damage Assessment")

        cv = report.get("cv")

        if cv:

            damage = cv[0]

            st.write(
                "**Image:**",
                damage["image_name"],
            )

            st.write(
                "**Severity:**",
                damage["severity"],
            )

            st.write(
                "**Repairable:**",
                damage["repairable"],
            )

            st.write("### Detected Objects")

            st.dataframe(
                damage["detections"],
                use_container_width=True,
            )

        st.divider()

        st.subheader("📝 NLP Summary")

        nlp = report.get("nlp")

        if nlp:

            st.write(
                "**Accident Type:**",
                nlp["accident_type"],
            )

            st.write(
                "**Vehicle Part:**",
                nlp["vehicle_part"],
            )

            st.write(
                "**Weather:**",
                nlp["weather"],
            )

            st.write(
                "**Severity:**",
                nlp["severity"],
            )

            st.write(
                "**Cause:**",
                nlp["cause"],
            )

        st.divider()

        st.subheader("🤖 CrewAI Executive Summary")

        if decision:

            summary = f"""
### Executive Summary

The claim **{claim_id}** has been analyzed by the IntelliClaim AI system.

• Computer Vision detected **{damage['severity']}** damage.

• NLP identified a **{nlp['accident_type']}** accident.

• Policy verification indicates the claim is **{decision['coverage']}**.

• Fraud score is **{decision['fraud_score']}**.

### Final Recommendation

✅ **{decision['decision']}**
"""

            st.markdown(summary)

            pdf_name = f"{claim_id}_report.pdf"

            generate_pdf(
                report,
                pdf_name,
            )

            with open(pdf_name, "rb") as pdf:

                st.download_button(
                    "📥 Download PDF Report",
                    pdf,
                    file_name=pdf_name,
                    mime="application/pdf",
                    use_container_width=True,
                )   