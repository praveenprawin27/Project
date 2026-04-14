import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT
)
""")

conn.commit()

def insert_job(title, company):
    cursor.execute("INSERT INTO jobs (title, company) VALUES (?, ?)", (title, company))
    conn.commit()

def view_jobs():
    cursor.execute("SELECT * FROM jobs")
    return cursor.fetchall()
