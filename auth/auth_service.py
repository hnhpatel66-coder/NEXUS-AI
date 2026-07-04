import sqlite3

from auth.password_manager import PasswordManager
from database.database import get_connection


class AuthService:

    # ==========================================
    # REGISTER USER
    # ==========================================
    @staticmethod
    def register_user(username, email, password):

        conn = get_connection()
        cursor = conn.cursor()

        # Email Exists?
        cursor.execute(
            "SELECT id FROM users WHERE email = ?",
            (email,)
        )

        if cursor.fetchone():
            conn.close()
            return False, "Email already exists."

        # Hash Password
        hashed_password = PasswordManager.hash_password(password)

        # Insert User
        cursor.execute(
            """
            INSERT INTO users
            (username, email, password)
            VALUES (?, ?, ?)
            """,
            (
                username,
                email,
                hashed_password
            )
        )

        conn.commit()
        conn.close()

        return True, "Registration Successful."

    # ==========================================
    # LOGIN USER
    # ==========================================
    @staticmethod
    def login_user(email, password):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE email = ?
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

    # ==========================================
    # GET USERNAME
    # ==========================================
    @staticmethod
    def get_username(email):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT username
            FROM users
            WHERE email = ?
            """,
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return user[0]

        return None