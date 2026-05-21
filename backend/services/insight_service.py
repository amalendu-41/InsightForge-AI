def generate_basic_insights(
    df,
    kpis,
    dimensions
):

    insights = []

    if kpis:

        metric = kpis[0]

        total = df[metric].sum()

        insights.append(
            f"Total {metric}: {round(total,2)}"
        )

    if dimensions and kpis:

        grouped = (
            df.groupby(dimensions[0])[kpis[0]]
            .sum()
            .reset_index()
        )

        top_category = grouped.sort_values(
            by=kpis[0],
            ascending=False
        ).iloc[0]

        insights.append(
            f"Top {dimensions[0]}: "
            f"{top_category[dimensions[0]]}"
        )

    return insights