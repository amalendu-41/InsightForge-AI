import ollama


def generate_ai_summary(df):

    sample_data = (
        df.head(10).to_string()
    )

    prompt = f"""
    You are a senior BI analyst.

    Analyze this dataset and provide:

    - Important KPIs
    - Trends
    - Business insights
    - Recommendations

    Dataset:

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

    return response["message"]["content"]