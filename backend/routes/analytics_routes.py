from fastapi import APIRouter
import pandas as pd

from backend.services.schema_service import (
    detect_kpis,
    detect_dimensions,
    detect_date_columns
)

from backend.services.kpi_service import (
    generate_kpi_metrics
)

router = APIRouter()


@router.get("/analyze")

def analyze_data(file_path: str):

    try:

        # -------------------------
        # Load file
        # -------------------------

        if file_path.endswith(".csv"):

            df = pd.read_csv(file_path)

        else:

            df = pd.read_excel(file_path)

        # -------------------------
        # Schema detection
        # -------------------------

        kpis = detect_kpis(df)

        dimensions = detect_dimensions(df)

        dates = detect_date_columns(df)

        # -------------------------
        # KPI Metrics
        # -------------------------

        metrics = {}

        if kpis:

            metrics = generate_kpi_metrics(
                df,
                kpis[0]
            )

        # -------------------------
        # Response
        # -------------------------

        return {

            "success": True,

            "kpis": kpis,

            "dimensions": dimensions,

            "dates": dates,

            "metrics": metrics
        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)
        }