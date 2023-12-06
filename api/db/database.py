import sqlite3


class Database:
    def __int__(self, db_file):
        self.connection = sqlite3.Connection(db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY, position TEXT, balance INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                                 (position TEXT, password TEXT)''')

    def get_user(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            return self.cursor.fetchone()

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users'").fetchall()

    def get_user_post(self, user_id):
        with self.connection:
            post = self.cursor.execute("SELECT position FROM 'users' WHERE 'user_id' = ?", user_id).fetchall()
            return post

    def get_user_token(self, user_id):
        with self.connection:
            token = self.cursor.execute("SELECT post FROM 'users' WHERE 'user_id' = ?", user_id).fetchall()
            return token

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", user_id).fetchall()
            return bool(len(result))

    def set_user_post(self, user_id, post):
        with self.connection:
            self.cursor.execute("UPDATE 'users' SET 'post' = ? WHERE 'user_id = ?'", (post, user_id))
            self.connection.commit()

    def set_user_token(self, user_id, token):
        with self.connection:
            self.cursor.execute("UPDATE 'users' SET 'balance' = ? WHERE 'user_id = ?'", (token, user_id))
            self.connection.commit()

    def get_post(self, user_id):
        with self.connection:
            post = self.cursor.execute("SELECT position FROM 'posts' WHERE 'user_id' = ?", user_id).fetchall()
            return post

    def get_pass(self, user_id):
        with self.connection:
            password = self.cursor.execute("SELECT password FROM 'posts' WHERE 'user_id' = ?", user_id).fetchall()
            return password

    def save_user(self, user_id, position, balance):
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' (id, position, balance) VALUES (?, ?, ?)",
                                (user_id, position, balance))
            self.connection.commit()

    def save_post(self, position, password):
        with self.connection:
            self.cursor.execute("INSERT INTO 'posts' (position, password) VALUES (?, ?)", (position, password))
            self.connection.commit()