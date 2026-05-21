def generate_kpi_metrics(
    df,
    metric_col
):

    return {

        "total": float(
            round(
                df[metric_col].sum(),
                2
            )
        ),

        "average": float(
            round(
                df[metric_col].mean(),
                2
            )
        ),

        "maximum": float(
            round(
                df[metric_col].max(),
                2
            )
        )
    }