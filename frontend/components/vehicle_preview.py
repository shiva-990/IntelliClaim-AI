import streamlit as st


def show_vehicle_preview():

    st.subheader("🚗 Latest Vehicle")

    st.image(
        "https://images.unsplash.com/photo-1503376780353-7e6692767b70",
        use_container_width=True,
    )