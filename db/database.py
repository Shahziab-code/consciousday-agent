import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "entries.db")

def init_db():
    """Initialize database and create table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            journal TEXT,
            intention TEXT,
            dream TEXT,
            priorities TEXT,
            reflection TEXT,
            strategy TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_entry(journal, intention, dream, priorities, reflection, strategy):
    """Save user entry into database."""
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (date, journal, intention, dream, priorities, reflection, strategy))
    conn.commit()
    conn.close()


def get_entries():
    """Retrieve all past entries."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
