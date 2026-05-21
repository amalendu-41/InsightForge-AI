import streamlit as st
import plotly.express as px


# --------------------------------
# LINE CHART
# --------------------------------

def create_line_chart(
    df,
    date_col,
    metric_col
):

    fig = px.line(

        df,

        x=date_col,

        y=metric_col,

        title=f"{metric_col} Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------
# BAR CHART
# --------------------------------

def create_bar_chart(
    df,
    dimension_col,
    metric_col
):

    grouped_df = (

        df.groupby(
            dimension_col
        )[metric_col]

        .sum()

        .reset_index()
    )

    fig = px.bar(

        grouped_df,

        x=dimension_col,

        y=metric_col,

        title=f"{metric_col} by {dimension_col}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------
# PIE CHART
# --------------------------------

def create_pie_chart(
    df,
    dimension_col,
    metric_col
):

    grouped_df = (

        df.groupby(
            dimension_col
        )[metric_col]

        .sum()

        .reset_index()
    )

    fig = px.pie(

        grouped_df,

        names=dimension_col,

        values=metric_col,

        title=f"{metric_col} Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------
# CHART RECOMMENDATION
# --------------------------------

def recommend_chart(
    date_cols,
    dimension_cols
):

    if date_cols:

        return "line"

    elif dimension_cols:

        return "bar"

    else:

        return "table"