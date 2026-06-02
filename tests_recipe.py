import pytest
from recipe_app.ingredient import Ingredient

def test_ingredient():
    ing = Ingredient(name="Мука", quantity=500.0, unit="г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient(name="Мука", quantity=500.0, unit="г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq():
    ing1 = Ingredient(name="Мука", quantity=500.0, unit="г")
    ing2 = Ingredient(name="Мука", quantity=300.0, unit="г")
    ing3 = Ingredient(name="Масло", quantity=500.0, unit="г")
    ing4 = Ingredient(name="Мука", quantity=500.0, unit="кг")

    assert ing1 == ing2
    assert ing1 != ing2
    assert ing1 != ing4




