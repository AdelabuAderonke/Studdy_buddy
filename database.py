import sqlite3
from datetime import datetime
def init_db():
    conn = sqlite3.connect("study_buddy.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            duration_seconds INTEGER,
            focused_pct REAL,
            confused_pct REAL,
            distracted_pct REAL
        )
    ''')
    conn.commit()
    conn.close()
def save_session(duration, focused, confused, distracted):
    conn = sqlite3.connect("study_buddy.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO sessions (date, duration_seconds, focused_pct, confused_pct, distracted_pct) VALUES (?, ?, ?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), duration, focused, confused, distracted))
    conn.commit()
    conn.close()
def get_all_sessions():
    conn = sqlite3.connect("study_buddy.db")
    c = conn.cursor()
    c.execute("SELECT * FROM sessions ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()
    return rows