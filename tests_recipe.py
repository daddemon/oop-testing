import pytest
from recipe_app.ingredient import Ingredient
from recipe_app.recipe import Recipe
from recipe_app.shopping_list import ShoppingList

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



def test_recipe():
    ing1 = Ingredient(name="Мука", quantity=240.0, unit="г")
    ing2 = Ingredient(name="Сахар", quantity=250.0, unit="г")
    recipe = Recipe(title="Демка кекса", ingredients=[ing1, ing2])

    assert recipe.title == "Демка кекса"
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[0].name == "Мука"

def test_add_ingredient():
    ing1 = Ingredient(name="Мука", quantity=240.0, unit="г")
    recipe = Recipe(title="Кекс", ingredients=[ing1])
    
    ing2 = Ingredient(name="Яйца", quantity=4.0, unit="шт.")
    recipe.add_ingredient(ing2)
    assert len(recipe.ingredients) == 2
    
    flour = Ingredient(name="Мука", quantity=60.0, unit="г")
    recipe.add_ingredient(flour)
    
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[0].quantity == 300.0

def test_scale():
    ing1 = Ingredient(name="Мука", quantity=100.0, unit="г")
    recipe = Recipe(title="Капкаке", ingredients=[ing1])
    
    scaled = recipe.scale(2.5)
    
    assert recipe.ingredients[0].quantity == 100.0
    assert isinstance(scaled, Recipe)
    assert scaled.ingredients[0].quantity == 250.0

def test_scale_error():
    ing1 = Ingredient(name="Мука", quantity=100.0, unit="г")
    recipe = Recipe(title="Капкаке", ingredients=[ing1])
    
    with pytest.raises(ValueError):
        recipe.scale(-1)  
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_len():
    ing1 = Ingredient(name="Мука", quantity=240.0, unit="г")
    ing2 = Ingredient(name="Сахар", quantity=250.0, unit="г")
    recipe = Recipe(title="Кексик", ingredients=[ing1, ing2])
    
    assert len(recipe) == 2
    exp_str = "Блюдо: Кексик\nСписок ингредиентов:\nМука: 240.0 г\nСахар: 250.0 г"
    assert str(recipe) == exp_str
