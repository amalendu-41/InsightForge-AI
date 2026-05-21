import streamlit as st

from services.api_client import (
    get_ai_summary
)


def show_insights():

    st.title("🤖 AI Insights")

    if "uploaded_path" not in st.session_state:

        st.warning(
            "Please upload dataset first."
        )

        return

    file_path = st.session_state[
        "uploaded_path"
    ]

    ai_summary = get_ai_summary(
        file_path
    )

    st.write(
        ai_summary["summary"]
    )