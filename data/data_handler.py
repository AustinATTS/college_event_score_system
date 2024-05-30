import sqlite3
from config.config import DATABASE_PATH


def create_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            individual_id INTEGER,
            individual_name TEXT,
            team_id INTEGER,
            team_name TEXT,
            team_memeber_one TEXT,
            team_member_two TEXT,
            team_member_three TEXT,
            team_memeber_four TEXT,
            team_member_five TEXT,
            event_one_name TEXT,
            event_one_type TEXT,
            event_one_rank INTEGER,
            event_two_name TEXT,
            event_two_type TEXT,
            event_two_rank INTEGER,
            event_three_name TEXT,
            event_three_type TEXT,
            event_three_rank INTEGER,
            event_four_name TEXT,
            event_four_type TEXT,
            event_four_rank INTEGER,
            event_five_name TEXT,
            event_five_type TEXT,
            event_five_rank INTEGER
        )
    ''')
    conn.commit()
    conn.close()


def insert_score(
    individual_id,
    individual_name,
    team_id,
    team_name,
    team_memeber_one,
    team_member_two,
    team_member_three,
    team_memeber_four,
    team_member_five,
    event_one_name,
    event_one_type,
    event_one_rank,
    event_two_name,
    event_two_type,
    event_two_rank,
    event_three_name,
    event_three_type,
    event_three_rank,
    event_four_name,
    event_four_type,
    event_four_rank,
    event_five_name,
    event_five_type,
    event_five_rank
):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scores (
            individual_id,
            individual_name,
            team_id,
            team_name,
            team_memeber_one,
            team_member_two,
            team_member_three,
            team_memeber_four,
            team_member_five,
            event_one_name,
            event_one_type,
            event_one_rank,
            event_two_name,
            event_two_type,
            event_two_rank,
            event_three_name,
            event_three_type,
            event_three_rank,
            event_four_name,
            event_four_type,
            event_four_rank,
            event_five_name,
            event_five_type,
            event_five_rank
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        individual_id,
        individual_name,
        team_id,
        team_name,
        team_memeber_one,
        team_member_two,
        team_member_three,
        team_memeber_four,
        team_member_five,
        event_one_name,
        event_one_type,
        event_one_rank,
        event_two_name,
        event_two_type,
        event_two_rank,
        event_three_name,
        event_three_type,
        event_three_rank,
        event_four_name,
        event_four_type,
        event_four_rank,
        event_five_name,
        event_five_type,
        event_five_rank)
            )
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
