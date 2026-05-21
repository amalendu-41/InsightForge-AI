import streamlit as st


def render_sidebar():

    st.sidebar.title("📊 AI BI Platform")

    page = st.sidebar.radio(

        "Navigation",

        [
            "Home",
            "Upload Dataset",
            "Dashboard",
            "AI Insights"
        ]
    )

    return page