from food_database import FOOD_DATABASE


def calculate_nutrition(food_name, quantity):
    """
    Calculate nutrition for a single food item.
    """

    food_name = food_name.lower()

    if food_name not in FOOD_DATABASE:
        return None

    food = FOOD_DATABASE[food_name]

    return {
        "calories": food["calories"] * quantity,
        "protein": food["protein"] * quantity,
        "carbs": food["carbs"] * quantity,
        "fat": food["fat"] * quantity,
        "fiber": food["fiber"] * quantity,
        "sugar": food["sugar"] * quantity
    }


def calculate_meal(food_items):
    """
    food_items example:

    [
        ("egg",2),
        ("bread",2),
        ("milk",1)
    ]
    """

    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "fiber": 0,
        "sugar": 0
    }

    for food_name, quantity in food_items:

        nutrition = calculate_nutrition(food_name, quantity)

        if nutrition is None:
            continue

        for key in totals:
            totals[key] += nutrition[key]

    return totals

if __name__ == "__main__":

    breakfast = [
        ("egg", 2),
        ("bread", 2),
        ("milk", 1)
    ]

    print(calculate_meal(breakfast))