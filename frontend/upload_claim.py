import streamlit as st
from datetime import date
import uuid

from utils.api_client import api


def show():

    st.title("📤 Upload Insurance Claim")

    st.divider()

    # -----------------------------
    # Customer Information
    # -----------------------------
    st.subheader("Customer Information")

    customers = api.get_customers()

    customer_options = [
        customer["customer_id"]
        for customer in customers
    ]

    customer_id = st.selectbox(
        "Customer",
        customer_options,
    )

    policies = api.get_policies()

    policy_options = [
        policy["policy_number"]
        for policy in policies
    ]

    policy_number = st.selectbox(
        "Policy",
        policy_options,
    )

    st.divider()

    # -----------------------------
    # Claim Information
    # -----------------------------
    st.subheader("Claim Information")

    accident_date = st.date_input(
        "Accident Date"
    )

    damage_type = st.selectbox(
        "Damage Type",
        [
            "Front Bumper",
            "Rear Bumper",
            "Door",
            "Bonnet",
            "Windshield",
            "Fender",
            "Light",
        ],
    )

    estimated_cost = st.number_input(
        "Estimated Repair Cost",
        min_value=0.0,
    )

    claim_amount = st.number_input(
        "Claim Amount",
        min_value=0.0,
    )

    st.divider()

    description = st.text_area(
        "Accident Description",
        height=150,
    )

    st.divider()

    # -----------------------------
    # Upload Image
    # -----------------------------
    image = st.file_uploader(
        "Upload Vehicle Image",
        type=["jpg", "jpeg", "png"],
    )

    if image:
        st.image(
            image,
            width=500,
        )

    st.divider()

    # -----------------------------
    # Submit Claim
    # -----------------------------
    if st.button(
        "🚀 Submit Claim",
        use_container_width=True,
    ):

        # Validation
        if image is None:
            st.error("Please upload a vehicle image.")
            return

        if not description.strip():
            st.error("Please enter an accident description.")
            return

        # Generate Claim ID
        claim_id = f"CLM-{uuid.uuid4().hex[:8].upper()}"

        payload = {

            "claim_id": claim_id,

            "customer_id": customer_id,

            "policy_number": policy_number,

            "accident_date": str(accident_date),

            "claim_date": str(date.today()),

            "damage_type": damage_type,

            "accident_description": description,

            "estimated_repair_cost": estimated_cost,

            "claim_amount": claim_amount,

            "fraud_label": "Pending",

            "fraud_score": 0,

            "claim_status": "Pending",

            "inspection_status": "Pending",

            "cv_status": "Pending",

            "nlp_status": "Pending",

            "rag_status": "Pending",

            "final_decision": "Pending",
        }

        progress = st.progress(0)

        # -----------------------------
        # Create Claim
        # -----------------------------
        st.write("📝 Creating Claim...")
        progress.progress(20)

        response = api.create_claim(payload)

        if response.status_code not in (200, 201):
            st.error(response.text)
            return

        # -----------------------------
        # Upload Image
        # -----------------------------
        st.write("📷 Uploading Vehicle Image...")
        progress.progress(50)

        upload = api.upload_image(
            claim_id,
            image,
        )
        st.write("Upload Status:", upload.status_code)
        st.write(upload.text)

        if upload.status_code != 200:
            st.error(upload.text)
            return

        # -----------------------------
        # Process Claim
        # -----------------------------
        st.write("🤖 Running AI Pipeline...")
        progress.progress(80)

        process = api.process_claim(
            claim_id
        )

        if process.status_code != 200:
            st.error(process.text)
            return

        progress.progress(100)

        st.success(
            "🎉 Insurance Claim Processed Successfully!"
        )

        st.balloons()

        st.info(
            f"Claim ID: **{claim_id}**"
        )