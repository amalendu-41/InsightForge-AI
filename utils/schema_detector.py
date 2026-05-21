import pandas as pd


# --------------------------------
# KPI PRIORITY
# --------------------------------

KPI_PRIORITY = {

    "revenue": 10,
    "sales": 9,
    "profit": 8,
    "amount": 7,
    "income": 7,
    "price": 6,
    "cost": 6,
    "quantity": 5,
    "value": 5
}


# --------------------------------
# KPI DETECTION
# --------------------------------

def detect_kpis(df):

    scored_kpis = []

    for col in df.columns:

        col_lower = col.lower()

        if pd.api.types.is_numeric_dtype(
            df[col]
        ):

            score = 0

            for keyword, priority in KPI_PRIORITY.items():

                if keyword in col_lower:

                    score = priority

            # Avoid IDs
            if "id" in col_lower:

                score = 0

            unique_ratio = (
                df[col].nunique()
                / len(df)
            )

            if unique_ratio < 0.9:

                score += 2

            if score > 0:

                scored_kpis.append(
                    (col, score)
                )

    scored_kpis.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return [
        col for col, score
        in scored_kpis
    ]


# --------------------------------
# DIMENSION DETECTION
# --------------------------------

def detect_dimensions(df):

    dimensions = []

    for col in df.columns:

        if (
            df[col].dtype == "object"
            and df[col].nunique() < 50
        ):

            dimensions.append(col)

    return dimensions


# --------------------------------
# DATE DETECTION
# --------------------------------

def detect_date_columns(df):

    date_cols = []

    for col in df.columns:

        if df[col].dtype == "object":

            try:

                converted = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

                valid_ratio = (
                    converted.notnull().sum()
                    / len(df)
                )

                if valid_ratio > 0.8:

                    date_cols.append(col)

            except:
                pass

    return date_cols