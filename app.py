import streamlit as st
from database import (
    create_connection,
    initialize_database,
    add_user
)
from models import User
from constants import (
    ACTIVITY_LEVELS,
    GOALS,
    GENDERS
)
initialize_database()

st.set_page_config(
    page_title="NutriCoach AI",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 NutriCoach AI")
st.write(
    "Your AI-powered nutrition and lifestyle companion."
)
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
    GENDERS
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
    ACTIVITY_LEVELS
)

goal = st.selectbox(
    "Goal",
    GOALS
)

if st.button("💾 Save Profile", use_container_width=True):

    if not name.strip():
        st.error("Please enter your name.")
        st.stop()

    user = User(
        name=name.strip(),
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        activity_level=activity_level,
        goal=goal
    )

    connection = create_connection()

    user_id = add_user(connection, user)

    connection.close()

    st.success(f"Profile saved successfully! User ID: {user_id}")
