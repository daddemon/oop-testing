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



def test_add_recipe():
    shopping_list = ShoppingList()
    ing = Ingredient(name="Мука", quantity=100.0, unit="г")
    recipe = Recipe(title="Шарлотка", ingredients=[ing])
    
    shopping_list.add_recipe(recipe, portions=2.0)
    
    assert len(shopping_list._items) == 1
    assert shopping_list._items[0][1] == "Шарлотка"
    assert shopping_list._items[0][0].quantity == 200.0

def test_add_error():
    shopping_list = ShoppingList()
    ing = Ingredient(name="Мука", quantity=100.0, unit="г")
    recipe = Recipe(title="Шарлотка", ingredients=[ing])
    
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, portions=-1)
        
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, portions=0)

def test_remove_recipe():
    shopping_list = ShoppingList()
    ing1 = Ingredient(name="Мука", quantity=100.0, unit="г")
    ing2 = Ingredient(name="Яйцо", quantity=2.0, unit="шт.")
    
    recipe1 = Recipe(title="Шарлотка", ingredients=[ing1])
    recipe2 = Recipe(title="Омлет", ingredients=[ing2])
    
    shopping_list.add_recipe(recipe1, portions=1.0)
    shopping_list.add_recipe(recipe2, portions=1.0)
    
    shopping_list.remove_recipe("Шарлотка")
    assert len(shopping_list._items) == 1
    assert shopping_list._items[0][1] == "Омлет"
    
    shopping_list.remove_recipe("Нет такого рецептика")
    assert len(shopping_list._items) == 1

def test_get_list():
    shopping_list = ShoppingList()
    
    ing1 = Ingredient(name="Сахар", quantity=100.0, unit="г")
    ing2 = Ingredient(name="Масло", quantity=50.0, unit="г")
    ing3 = Ingredient(name="Сахар", quantity=150.0, unit="г")
    
    recipe1 = Recipe(title="Печенье", ingredients=[ing1, ing2])
    recipe2 = Recipe(title="Баблти", ingredients=[ing3])
    
    shopping_list.add_recipe(recipe1, portions=1.0)
    shopping_list.add_recipe(recipe2, portions=1.0)
    
    end_list = shopping_list.get_list()
    
    assert len(end_list) == 2
    
    assert end_list[0].name == "Масло"
    assert end_list[0].quantity == 50.0
    
    assert end_list[1].name == "Сахар"
    assert end_list[1].quantity == 250.0

def test_shopping_list_add():
    l1 = ShoppingList()
    l2 = ShoppingList()
    
    ing1 = Ingredient(name="Мука", quantity=100.0, unit="г")
    ing2 = Ingredient(name="Сахар", quantity=200.0, unit="г")
    
    rec1 = Recipe(title="Пирог", ingredients=[ing1])
    rec2 = Recipe(title="Торт", ingredients=[ing2])
    
    l1.add_recipe(rec1, portions=1.0)
    l2.add_recipe(rec2, portions=1.0)
    
    lists = l1 + l2
    
    assert len(lists._items) == 2
    assert len(l1._items) == 1
    assert len(l2._items) == 1