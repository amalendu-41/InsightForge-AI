from fastapi import APIRouter
import pandas as pd

from backend.services.ai_service import (
    generate_ai_summary
)

router = APIRouter()


@router.get("/ai-summary")

def ai_summary(file_path: str):

    if file_path.endswith(".csv"):

        df = pd.read_csv(file_path)

    else:

        df = pd.read_excel(file_path)

    summary = generate_ai_summary(df)

    return {
        "summary": summary
    }