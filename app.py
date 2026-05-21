import streamlit as st
import pandas as pd

from utils.file_handler import load_file

from utils.schema_detector import (
    detect_kpis,
    detect_dimensions,
    detect_date_columns
)

from utils.kpi_engine import generate_kpi_metrics

from utils.chart_generator import (
    create_line_chart,
    create_bar_chart,
    create_pie_chart,
    recommend_chart
)

from utils.insight_engine import (
    generate_basic_insights
)

from utils.ai_engine import (
    generate_ai_summary
)

# --------------------------------

st.set_page_config(
    page_title="AI BI Dashboard",
    layout="wide"
)

st.title("📊 AI-Powered BI Dashboard Generator")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

# --------------------------------

if uploaded_file is not None:

    # Load file
    df = load_file(uploaded_file)

    st.success("File Uploaded Successfully!")

    # --------------------------------
    # Preview
    # --------------------------------

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # --------------------------------
    # Schema Detection
    # --------------------------------

    kpis = detect_kpis(df)

    dimensions = detect_dimensions(df)

    dates = detect_date_columns(df)

    # Convert date column properly
    if dates:

        df[dates[0]] = pd.to_datetime(
            df[dates[0]]
        )

    # Debugging
    st.write("KPIs:", kpis)

    st.write("Dimensions:", dimensions)

    st.write("Dates:", dates)

    # --------------------------------
    # KPI Cards
    # --------------------------------

    if kpis:

        metrics = generate_kpi_metrics(
            df,
            kpis[0]
        )

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

    # --------------------------------
    # Intelligent Visualization Engine
    # --------------------------------

    st.subheader("📈 Intelligent Visualizations")

    recommended_chart = recommend_chart(
        dates,
        dimensions
    )

    st.write(
        "Recommended Chart Type:",
        recommended_chart
    )

    # --------------------------------
    # Line Chart
    # --------------------------------

    if recommended_chart == "line":

        if dates and kpis:

            create_line_chart(
                df,
                dates[0],
                kpis[0]
            )

    # --------------------------------
    # Bar Chart
    # --------------------------------

    elif recommended_chart == "bar":

        if dimensions and kpis:

            create_bar_chart(
                df,
                dimensions[0],
                kpis[0]
            )

            create_pie_chart(
                df,
                dimensions[0],
                kpis[0]
            )

    # --------------------------------
    # Fallback
    # --------------------------------

    else:

        st.dataframe(df.head())

    # --------------------------------
    # Rule-Based Insights
    # --------------------------------

    st.subheader("🤖 AI Insights")

    insights = generate_basic_insights(
        df,
        kpis,
        dimensions
    )

    for insight in insights:

        st.success(insight)

    # --------------------------------
    # LLM AI Summary
    # --------------------------------

    st.subheader("🧠 AI Business Summary")

    with st.spinner(
        "Generating AI insights..."
    ):

        summary = generate_ai_summary(df)

        st.write(summary)

else:

    st.info(
        "Please upload a CSV or Excel file."
    )