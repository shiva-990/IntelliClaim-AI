import streamlit as st
from utils.api_client import api


def show_cards():

    claims = api.get_claims()

    total = len(claims)

    approved = 0
    rejected = 0
    manual = 0
    fraud = 0
    total_cost = 0

    for claim in claims:

        status = claim.get("claim_status", "").lower()

        if status == "approved":
            approved += 1

        elif status == "rejected":
            rejected += 1

        else:
            manual += 1

        if claim.get("fraud_score", 0) >= 70:
            fraud += 1

        total_cost += claim.get("estimated_repair_cost", 0)

    avg_cost = total_cost / total if total else 0

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.metric("📄 Total Claims", total)
    c2.metric("✅ Approved", approved)
    c3.metric("❌ Rejected", rejected)
    c4.metric("🟡 Review", manual)
    c5.metric("🚨 Fraud", fraud)
    c6.metric("💰 Avg Repair", f"₹{avg_cost:,.0f}")