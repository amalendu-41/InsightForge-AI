import streamlit as st


def show_home():
    st.title(
        "📊 AI-Powered BI Dashboard Generator"
    )

    st.markdown("""

    Transform raw datasets into:

    - Interactive dashboards
    - KPI insights
    - AI-generated recommendations
    - Trend analysis

    """)

    # -------------------------
    # Metrics
    # -------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Supported Files",
        "CSV/XLSX"
    )

    col2.metric(
        "AI Engine",
        "Llama3"
    )

    col3.metric(
        "Charts",
        "Dynamic"
    )

    col4.metric(
        "Insights",
        "Automated"
    )

    st.divider()

    st.subheader("🚀 Platform Features")

    st.markdown("""

    ✅ Automated KPI Detection

    ✅ Intelligent Chart Generation

    ✅ AI Business Insights

    ✅ Trend Analysis

    ✅ FastAPI Backend

    ✅ SQLite Persistence

    """)
    