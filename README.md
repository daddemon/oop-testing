# oop-testing

# Cистема для управления рецептами

## Описание

Это консольное приложение, которое позволяет создавать блюда, добавлять их в "рецепты", масштабировать порции и генерировать список покупок.

## Использование

### 1. Установка

Склонируйте репозиторий с проектом к себе на компьютер и перейдите в папку проекта:

   ```bash
   git clone <ссылка_на_твой_репозиторий>
   cd <название_папки_проекта>
   ```

Установите все необходимые зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```

### 2. Классы

Вы можете использовать классы в своём коде. 
Важные импорты:

```python
from recipe_app.ingredient import Ingredient
from recipe_app.recipe import Recipe
from recipe_app.shopping_list import ShoppingList

#Занесём ингредиент в нашу систему:

flour = Ingredient(name="Мука", quantity=200.0, unit="г")
sugar = Ingredient(name="Сахар", quantity=100.0, unit="г")

#Создадим рецепт:

cake = Recipe(title="Кексик", ingredients=[flour, sugar])

# Создадим список покупок и добавим рецепт на 2 порции:

my_shopping_list = ShoppingList()
my_shopping_list.add_recipe(cake, portions=2.0)

# Получим итоговый список ингредиентов (с учётом всех рецептов):
fin_ingredients = my_shopping_list.get_list()
for ing in fin_ingredients:
    print(ing)
```
### 3. Тесты

Чтобы запустить тесты, убедитесь, что у вас установлен pytest. Если его нет, используйте команду:

```bash
pip install pytest
```

После этого тесты нужно запустить в корневой папке:

```python
pytest

#Если возникает ошибка, попробуйте этот вариант:

python -m pytest
```


## Автор проекта

`Ордынская М.В.`, группа `БТАДБ251`