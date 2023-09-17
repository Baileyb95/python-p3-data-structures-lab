spicy_fooder = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = []
    for spicy_food in spicy_foods:
        spicy_foods_names.append(spicy_food["name"])
    return spicy_foods_names
    

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] >= 5:
            spiciest_foods.append(spicy_food)
    return spiciest_foods

    
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
        print
    return "No such food"


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for index in range(0, len(spiciest_foods)):
            print(f"{spiciest_foods[index]['name']} ({spiciest_foods[index]['cuisine']}) | Heat Level: {(spiciest_foods[index]['heat_level'] * '🌶')}")
        # return(f"{spiciest_foods[index]['name']} ({spiciest_foods[index]['cuisine']}) | Heat Level: {spiciest_foods[index]['heat_level'] * '🌶' }")


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for spicy_food in spicy_foods:
        total_heat_level += spicy_food["heat_level"]
    return total_heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print_spiciest_foods(spicy_fooder)
