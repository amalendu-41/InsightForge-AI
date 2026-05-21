from backend.database.db import (
    get_connection
)


# --------------------------------
# CREATE TABLES
# --------------------------------

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # --------------------------------
    # Uploaded Files Table
    # --------------------------------

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS uploaded_files (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT NOT NULL,

        file_path TEXT NOT NULL,

        upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # --------------------------------
    # AI Insights Table
    # --------------------------------

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS ai_insights (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        summary TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # --------------------------------
    # Dashboard History Table
    # --------------------------------

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS dashboard_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        kpis TEXT,

        dimensions TEXT,

        dates TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    conn.commit()

    conn.close()


# --------------------------------
# INSERT UPLOADED FILE
# --------------------------------

def save_uploaded_file(
    filename,
    file_path
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO uploaded_files (

        filename,
        file_path

    )

    VALUES (?, ?)

    """,

    (
        filename,
        file_path
    ))

    conn.commit()

    conn.close()


# --------------------------------
# SAVE AI INSIGHT
# --------------------------------

def save_ai_insight(
    filename,
    summary
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO ai_insights (

        filename,
        summary

    )

    VALUES (?, ?)

    """,

    (
        filename,
        summary
    ))

    conn.commit()

    conn.close()


# --------------------------------
# SAVE DASHBOARD METADATA
# --------------------------------

def save_dashboard_metadata(

    filename,

    kpis,

    dimensions,

    dates
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""INSERT INTO dashboard_history (filename, kpis, dimensions, dates ) VALUES (?, ?, ?, ?)""",

    (
        filename, str(kpis), str(dimensions), str(dates)
))

    conn.commit()

    conn.close()