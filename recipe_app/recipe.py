from dataclasses import dataclass
from recipe_app.ingredient import Ingredient

@dataclass
class Recipe:
    title: str
    ingredients: list

    def add_ingredient(self, ingredient: Ingredient):
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
      scaled_ing = []
      for ing in self.ingredients:
          new_ing = Ingredient(name=ing.name, quantity=ing.quantity * ratio, unit=ing.unit)
          scaled_ing.append(new_ing)
        
        return Recipe(title=self.title, ingredients=scaled_ing)
