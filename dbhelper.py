import sqlite3

class Dbhelper:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.create_table()

    def create_table(self):
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users
                                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  name TEXT,
                                  email TEXT UNIQUE,
                                  password TEXT)''')
            self.conn.commit()
        except Exception as e:
            print(e)

    def register(self, name, email, password):
        try:
            self.conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def search(self, email, password):
        cursor = self.conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user_details = cursor.fetchall()
        return user_details if user_details else None
