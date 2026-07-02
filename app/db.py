import sqlite3

conn = sqlite3.connect("bot.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    model TEXT,
    trade_in INTEGER,
    doplata INTEGER
)
""")

conn.commit()


def save_lead(name, phone, model, trade_in, doplata):
    cur.execute("""
        INSERT INTO leads (name, phone, model, trade_in, doplata)
        VALUES (?, ?, ?, ?, ?)
    """, (name, phone, model, trade_in, doplata))
    conn.commit()