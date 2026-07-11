import streamlit as st
from database import (
    create_connection,
    initialize_database,
    add_user
)

initialize_database()

st.set_page_config(
    page_title="NutriCoach AI",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 NutriCoach AI")

st.subheader("Create Your Profile")

name = st.text_input("Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    step=1
)

gender = st.selectbox(
    "Gender",
    [
        "Male",
        "Female",
        "Other"
    ]
)

height = st.number_input(
    "Height (cm)",
    min_value=50.0,
    max_value=250.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=300.0
)

activity_level = st.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ]
)

goal = st.selectbox(
    "Goal",
    [
        "Lose Fat",
        "Maintain Weight",
        "Gain Muscle"
    ]
)

if st.button("Save Profile"):

    connection = create_connection()

    user_id = add_user(
        connection,
        name,
        age,
        gender,
        height,
        weight,
        activity_level,
        goal
    )

    connection.close()

    st.success(f"Profile saved successfully! User ID: {user_id}")