import sqlite3
from config.config import DATABASE_PATH


def solo_create_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS solo_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_type TEXT,
            individual_id INTEGER,
            individual_name TEXT,
            team_id INTEGER,
            team_name TEXT,
            team_member_one TEXT,
            team_member_two TEXT,
            team_member_three TEXT,
            team_member_four TEXT,
            team_member_five TEXT,
            solo_event_name TEXT,
            solo_event_type TEXT,
            solo_event_rank INTEGER
        )
    ''')
    conn.commit()
    conn.close()


def solo_insert_score(participant_type,
                      individual_id,
                      individual_name,
                      team_id,
                      team_name,
                      team_member_one,
                      team_member_two,
                      team_member_three,
                      team_member_four,
                      team_member_five,
                      solo_event_name,
                      solo_event_type,
                      solo_event_rank):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO solo_scores (participant_type,
                                 individual_id,
                                 individual_name,
                                 team_id,
                                 team_name,
                                 team_member_one,
                                 team_member_two,
                                 team_member_three,
                                 team_member_four,
                                 team_member_five,
                                 solo_event_name,
                                 solo_event_type,
                                 solo_event_rank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (participant_type,
          individual_id,
          individual_name,
          team_id,
          team_name,
          team_member_one,
          team_member_two,
          team_member_three,
          team_member_four,
          team_member_five,
          solo_event_name,
          solo_event_type,
          solo_event_rank))
    conn.commit()
    conn.close()


def solo_fetch_scores():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM solo_scores')
    rows = cursor.fetchall()
    conn.close()
    return rows


def solo_clear_scores():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM solo_scores')
    conn.commit()
    conn.close()


solo_create_table()
