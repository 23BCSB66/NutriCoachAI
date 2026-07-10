import sqlite3

DATABASE_NAME = "data/nutricoach.db"


def create_connection():
    """Create and return a connection to the SQLite database."""

    try:
        connection = sqlite3.connect(DATABASE_NAME)
        return connection

    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

def create_tables(connection):
    """Create all required database tables."""

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        height REAL NOT NULL,
        weight REAL NOT NULL,
        activity_level TEXT NOT NULL,
        goal TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        date TEXT NOT NULL,

        meal_type TEXT NOT NULL,

        food_name TEXT NOT NULL,

        quantity REAL NOT NULL,

        estimated_calories REAL NOT NULL,

        estimated_protein REAL NOT NULL,

        estimated_carbs REAL NOT NULL,

        estimated_fat REAL NOT NULL,

        estimated_fiber REAL NOT NULL,

        estimated_sugar REAL NOT NULL,

        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    connection.commit()

def initialize_database():
    """Initialize the database and create tables."""

    connection = create_connection()

    if connection:
        create_tables(connection)
        connection.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")