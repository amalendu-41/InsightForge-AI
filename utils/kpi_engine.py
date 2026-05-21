def generate_kpi_metrics(
    df,
    metric_col
):

    metrics = {

        "total": round(
            df[metric_col].sum(),
            2
        ),

        "average": round(
            df[metric_col].mean(),
            2
        ),

        "maximum": round(
            df[metric_col].max(),
            2
        )
    }

    return metrics