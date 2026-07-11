from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    name: str
    age: int
    gender: str
    height: float
    weight: float
    activity_level: str
    goal: str


@dataclass
class FoodLog:
    user_id: int
    date: date
    meal_type: str
    food_name: str
    quantity: float