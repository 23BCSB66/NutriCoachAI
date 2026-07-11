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

def add_user(connection, name, age, gender, height, weight, activity_level, goal):
    """
    Add a new user to the database.
    Returns the newly created user's ID.
    """

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (
            name,
            age,
            gender,
            height,
            weight,
            activity_level,
            goal
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        age,
        gender,
        height,
        weight,
        activity_level,
        goal
    ))

    connection.commit()

    return cursor.lastrowid


def get_user(connection, user_id):
    """
    Retrieve a user by ID.
    """

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE id = ?
    """, (user_id,))

    return cursor.fetchone()


def update_user(connection, user_id, weight, activity_level, goal):
    """
    Update editable user fields.
    """

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET
            weight = ?,
            activity_level = ?,
            goal = ?
        WHERE id = ?
    """, (
        weight,
        activity_level,
        goal,
        user_id
    ))

    connection.commit()


def delete_user(connection, user_id):
    """
    Delete a user from the database.
    """

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE id = ?
    """, (user_id,))

    connection.commit()

def initialize_database():
    """Initialize the database."""

    connection = create_connection()

    if connection:
        create_tables(connection)
        connection.close()

if __name__ == "__main__":

    initialize_database()

    connection = create_connection()

    print("=== ADD USER ===")

    user_id = add_user(
        connection,
        "Asish",
        21,
        "Male",
        173,
        70,
        "Moderately Active",
        "Gain Muscle"
    )

    print(f"User created with ID: {user_id}")

    print("\n=== GET USER ===")

    user = get_user(connection, user_id)

    print(user)

    print("\n=== UPDATE USER ===")

    update_user(
        connection,
        user_id,
        72,
        "Very Active",
        "Maintain Weight"
    )

    print(get_user(connection, user_id))

    print("\n=== DELETE USER ===")

    delete_user(connection, user_id)

    print(get_user(connection, user_id))

    connection.close()