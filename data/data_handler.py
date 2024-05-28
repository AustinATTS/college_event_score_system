import sqlite3
from config.config import DATABASE_PATH


def create_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            individual_id INTEGER NOT NULL,
            individual_name TEXT NOT NULL,
            event_one_name TEXT NOT NULL,
            event_one_rank INTEGER NOT NULL,
            event_two_name TEXT NOT NULL,
            event_two_rank INTEGER NOT NULL,
            event_three_name TEXT NOT NULL,
            event_three_rank INTEGER NOT NULL,
            event_four_name TEXT NOT NULL,
            event_four_rank INTEGER NOT NULL,
            event_five_name TEXT NOT NULL,
            event_five_rank INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insert_score(individual_id, individual_name, event_one_name, event_one_rank, event_two_name, event_two_rank, event_three_name, event_three_rank, event_four_name, event_four_rank, event_five_name, event_five_rank):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scores (individual_id, individual_name, event_one_name, event_one_rank, event_two_name, event_two_rank, event_three_name, event_three_rank, event_four_name, event_four_rank, event_five_name, event_five_rank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (individual_id, individual_name, event_one_name, event_one_rank, event_two_name, event_two_rank, event_three_name, event_three_rank, event_four_name, event_four_rank, event_five_name, event_five_rank))
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
