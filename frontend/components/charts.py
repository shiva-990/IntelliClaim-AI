import streamlit as st
import plotly.express as px
import pandas as pd


def show_charts():

    left, right = st.columns(2)

    with left:

        df = pd.DataFrame(
            {
                "Month": [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                ],
                "Claims": [
                    25,
                    35,
                    42,
                    58,
                    63,
                    74,
                ],
            }
        )

        fig = px.line(
            df,
            x="Month",
            y="Claims",
            markers=True,
            title="Claims Overview",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with right:

        pie = pd.DataFrame(
            {
                "Status": [
                    "Approved",
                    "Rejected",
                    "Manual Review",
                ],
                "Count": [
                    180,
                    25,
                    25,
                ],
            }
        )

        fig2 = px.pie(
            pie,
            names="Status",
            values="Count",
            title="Claim Status",
        )

        st.plotly_chart(
            fig2,
            use_container_width=True,
        )