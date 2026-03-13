# Database Initialization Code for Eagle Accounting System

import sqlite3

def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('eagle_accounting.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY,
                      username TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL
                     )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER,
                      amount REAL NOT NULL,
                      transaction_date TEXT NOT NULL,
                      FOREIGN KEY(user_id) REFERENCES users(id)
                     )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()