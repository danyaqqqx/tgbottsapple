import sqlite3
from datetime import datetime

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    phone TEXT,
    model TEXT,
    trade_in INTEGER,
    created_at TEXT
)
""")

conn.commit()


def save_lead(user_id, name, phone, model, trade_in):
    cur.execute("""
        INSERT INTO leads (user_id, name, phone, model, trade_in, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, name, phone, model, trade_in, datetime.now().isoformat()))
    conn.commit()


def get_lead(user_id):
    cur.execute("SELECT * FROM leads WHERE user_id=?", (user_id,))
    return cur.fetchone()