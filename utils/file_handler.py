import pandas as pd


def load_file(uploaded_file):

    if uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):

        df = pd.read_excel(uploaded_file)

    else:

        raise ValueError(
            "Unsupported file type"
        )

    return df