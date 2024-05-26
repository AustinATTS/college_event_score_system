import sqlite3
from config.config import DATABASE_PATH


def create_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_name TEXT NOT NULL,
            event_name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insert_score(participant_name, event_name, score):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scores (participant_name, event_name, score)
        VALUES (?, ?, ?)
    ''', (participant_name, event_name, score))
    conn.commit()
    conn.close()


def fetch_scores():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scores')
    rows = cursor.fetchall()
    conn.close()
    return rows


def clear_scores():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM scores')
    conn.commit()
    conn.close()


create_table()
