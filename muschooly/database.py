import sqlite3

conn = sqlite3.connect('bot.db')
cursor = conn.cursor()

# Add message_id to responses table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        message_id INTEGER,
        selected_answer TEXT,
        is_correct INTEGER,
        timestamp DATETIME
    )
''')

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        is_subscribed INTEGER DEFAULT 1,
        is_admin INTEGER DEFAULT 0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pictures (
        picture_id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        question_text TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sent_messages (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        picture_id INTEGER,
        sent_time DATETIME,
        user_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        message_id INTEGER,
        selected_answer TEXT,
        is_correct INTEGER,
        timestamp DATETIME
    )
''')

conn.commit()
conn.close()
