import streamlit as st

from services.api_client import (
    upload_file
)


def show_upload():

    st.title("📤 Upload Dataset")

    uploaded_file = st.file_uploader(

        "Upload CSV or Excel",

        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        response = upload_file(
            uploaded_file
        )

        st.success(
            "File uploaded successfully!"
        )

        st.session_state[
            "uploaded_path"
        ] = response["path"]

        st.session_state[
            "uploaded_filename"
        ] = response["filename"]
