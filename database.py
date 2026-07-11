import sqlite3
from nutrition import calculate_nutrition

DATABASE_NAME = "data/nutricoach.db"

def initialize_database():
    """Initialize the database."""

    connection = create_connection()

    if connection:
        create_tables(connection)
        connection.close()

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

def add_food_log(
    connection,
    user_id,
    date,
    meal_type,
    food_name,
    quantity,
    nutrition
):
    """
    Add a food log entry.
    """

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO food_logs(
            user_id,
            date,
            meal_type,
            food_name,
            quantity,
            estimated_calories,
            estimated_protein,
            estimated_carbs,
            estimated_fat,
            estimated_fiber,
            estimated_sugar
        )

        VALUES(
            ?,?,?,?,?,?,?,?,?,?,?
        )
    """,(
        user_id,
        date,
        meal_type,
        food_name,
        quantity,
        nutrition["calories"],
        nutrition["protein"],
        nutrition["carbs"],
        nutrition["fat"],
        nutrition["fiber"],
        nutrition["sugar"]
    ))

def get_food_logs(connection, user_id):
    """
    Retrieve all food logs for a user.
    """

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM food_logs
        WHERE user_id = ?
    """, (user_id,))

    return cursor.fetchall()

if __name__ == "__main__":

    initialize_database()

    connection = create_connection()

    # Create a test user
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

    # Calculate nutrition
    nutrition = calculate_nutrition("egg", 2)

    # Store the meal
    add_food_log(
        connection,
        user_id,
        "2026-07-12",
        "Breakfast",
        "egg",
        2,
        nutrition
    )

    # Display everything
    print("\nFood Logs:\n")

    logs = get_food_logs(connection, user_id)

    for log in logs:
        print(log)

    connection.close()