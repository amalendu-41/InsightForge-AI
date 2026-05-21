import streamlit as st
import pandas as pd
import plotly.express as px

from services.api_client import (
    get_analytics
)


def show_dashboard():

    st.title("📈 Dashboard")

    if "uploaded_path" not in st.session_state:

        st.warning(
            "Please upload dataset first."
        )

        return

    file_path = st.session_state[
        "uploaded_path"
    ]

    analytics = get_analytics(
        file_path
    )

    # -------------------------
    # API Error Handling
    # -------------------------

    if not analytics.get("success"):

        st.error(
            f"Backend Error: {analytics.get('error')}"
        )

        return

    st.subheader("Detected Schema")

    st.write(
        "KPIs:",
        analytics["kpis"]
    )

    st.write(
        "Dimensions:",
        analytics["dimensions"]
    )

    st.write(
        "Dates:",
        analytics["dates"]
    )

    metrics = analytics["metrics"]

    if metrics:

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total",
            metrics["total"]
        )

        col2.metric(
            "Average",
            metrics["average"]
        )

        col3.metric(
            "Maximum",
            metrics["maximum"]
        )

    # -------------------------
    # Load dataset
    # -------------------------

    if file_path.endswith(".csv"):

        df = pd.read_csv(file_path)

    else:

        df = pd.read_excel(file_path)

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # -------------------------
    # Charts
    # -------------------------

    if (
        analytics["dates"]
        and analytics["kpis"]
    ):

        date_col = analytics["dates"][0]

        kpi_col = analytics["kpis"][0]

        df[date_col] = pd.to_datetime(
            df[date_col]
        )

        fig = px.line(

            df,

            x=date_col,

            y=kpi_col,

            title=f"{kpi_col} Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )