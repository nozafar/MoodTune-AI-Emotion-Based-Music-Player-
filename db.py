import sqlite3

def init_db():
    con = sqlite3.connect("moodtune.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )""")
    con.commit()
    con.close()

def add_user(username, password):
    con = sqlite3.connect("moodtune.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users(username,password) VALUES(?,?)",(username,password))
    con.commit()
    con.close()

def login_user(username, password):
    con = sqlite3.connect("moodtune.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    r = cur.fetchone()
    con.close()
    return r
