import pytest
from praktikum.ingredient import Ingredient
from constants import INGREDIENT_INIT_CASES

class TestIngredient:
    """Юнит-тесты для класса Ingredient."""

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_init_creates_instance(self, ingredient_type, name, price):
        """Конструктор создаёт корректный экземпляр Ingredient."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient, Ingredient)

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_init_saves_type(self, ingredient_type, name, price):
        """Конструктор корректно сохраняет тип ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_init_saves_name(self, ingredient_type, name, price):
        """Конструктор корректно сохраняет название ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.name == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_init_saves_price(self, ingredient_type, name, price):
        """Конструктор корректно сохраняет цену ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.price == price

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_get_type_returns_type(self, ingredient_type, name, price):
        """get_type возвращает тип ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_get_name_returns_name(self, ingredient_type, name, price):
        """get_name возвращает название ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_INIT_CASES)
    def test_get_price_returns_price(self, ingredient_type, name, price):
        """get_price возвращает цену ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
