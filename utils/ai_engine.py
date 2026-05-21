import ollama


def generate_ai_summary(df):

    sample_data = (
        df.head(10).to_string()
    )

    prompt = f"""
    You are a senior Business Intelligence Analyst.

    Analyze the dataset and provide:

    1. Important KPIs
    2. Trends
    3. Anomalies
    4. Business insights
    5. Recommendations

    Dataset Sample:

    {sample_data}
    """

    response = ollama.chat(

        model="llama3",

        messages=[

            {
                "role": "user",

                "content": prompt
            }
        ]
    )

    return response[
        "message"
    ]["content"]