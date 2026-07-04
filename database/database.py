import sqlite3
from pathlib import Path


# ==========================================
# Database Configuration
# ==========================================

DATABASE_DIR = Path("database")
DATABASE_FILE = DATABASE_DIR / "nexus_ai.db"


# ==========================================
# Database Connection
# ==========================================

def get_connection():

    DATABASE_DIR.mkdir(exist_ok=True)

    return sqlite3.connect(DATABASE_FILE)


# ==========================================
# Create Database
# ==========================================

def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    # --------------------------------------
    # Users Table
    # --------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # --------------------------------------
    # Chat History
    # --------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_email TEXT,

            sender TEXT,

            message TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# Reset Database (Developer Only)
# ==========================================

def reset_database():

    if DATABASE_FILE.exists():
        DATABASE_FILE.unlink()

    create_database()


# ==========================================
# Test
# ==========================================

if __name__ == "__main__":

    create_database()

    print("✅ Database Created Successfully")