import sqlite3

from auth.password_manager import PasswordManager
from database.database import DB_PATH


class AuthService:

    @staticmethod
    def register_user(full_name, email, password):

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE email=?",
            (email,)
        )

        if cursor.fetchone():
            conn.close()
            return False, "Email already exists."

        hashed_password = PasswordManager.hash_password(password)

        cursor.execute(
            """
            INSERT INTO users(full_name,email,password)
            VALUES(?,?,?)
            """,
            (
                full_name,
                email,
                hashed_password
            )
        )

        conn.commit()
        conn.close()

        return True, "Registration Successful."

    @staticmethod
    def login_user(email, password):

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE email=?
            """,
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user is None:
            return False

        return PasswordManager.verify_password(
            password,
            user[0]
        )