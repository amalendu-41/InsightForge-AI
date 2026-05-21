import sqlite3


def get_connection():

    conn = sqlite3.connect(
        "backend/database/app.db"
    )

    return conn