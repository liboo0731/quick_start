#!/usr/bin/python

import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('hello.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS TODOS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT UNIQUE NOT NULL,
TITLE TEXT NOT NULL,
NUM INT);''')
    conn.commit()
    conn.close()
