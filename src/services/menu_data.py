import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient
# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding='UTF-8') as file:
            reader = csv.DictReader(file)

            menu = {}
            for row in reader:
                dish_menu = row['dish']
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])
                price = float(row['price'])

                if dish_menu not in menu:
                    new_dish = Dish(dish_menu, price)
                    menu[dish_menu] = new_dish
                else:
                    new_dish = menu[dish_menu]

                new_ingredient = Ingredient(ingredient_name)
                new_dish.add_ingredient_dependency(
                    new_ingredient,
                    recipe_amount
                )
        self.dishes = set(menu.values())
