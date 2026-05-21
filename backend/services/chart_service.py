def recommend_chart(
    dates,
    dimensions
):

    if dates:

        return "line"

    elif dimensions:

        return "bar"

    return "table"