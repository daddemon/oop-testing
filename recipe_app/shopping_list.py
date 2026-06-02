from recipe_app.ingredient import Ingredient
from recipe_app.recipe import Recipe
from recipe_app.recipe import DietaryRecipe

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, scaled_recipe.title))

    def remove_recipe(self, title: str):
        self._items = [i for i in self._items if i[1] != title]

    def get_list(self):
        t = {}
        for ing in self._items:
            i = ing[0]
            key = (i.name, i.unit)
            if key in t:
                t[key] += i.quantity
            else:
                t[key] = i.quantity

        end_list = []
        for (name, unit), quantity in t.items():
            new_ing = Ingredient(name=name, quantity=quantity, unit=unit)
            end_list.append(new_ing)

        end_list.sort(key=lambda x: x.name)
        return end_list
        
    def __add__(self, other: "ShoppingList"):
        lists = ShoppingList()
        lists._items = self._items + other._items
        return lists
