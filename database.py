import sqlite3

DB_NAME = "bot.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            full_name TEXT,
            username TEXT,
            balance REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, full_name, username):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users
        (user_id, full_name, username)
        VALUES (?, ?, ?)
    """, (user_id, full_name, username))

    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else 0