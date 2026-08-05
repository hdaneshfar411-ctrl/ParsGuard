import sqlite3

DB_NAME = "parsguard.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        protocol TEXT NOT NULL,
        traffic INTEGER NOT NULL,
        expire INTEGER NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
