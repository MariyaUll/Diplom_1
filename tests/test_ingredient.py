import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestIngredient:
    """Юнит-тесты для класса Ingredient."""

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
            ("SAUCE", "", 0),
            ("FILLING", "cheese", 50.5),
        ],
    )
    def test_init_ingredient_attributes(self, ingredient_type, name, price):
        """Конструктор корректно сохраняет тип, название и цену."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            ("SAUCE", "", 0),
            ("FILLING", "cheese", 50.5),
        ],
    )
    def test_get_price_returns_price(self, ingredient_type, name, price):
        """get_price возвращает цену ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            ("SAUCE", "", 0),
            ("FILLING", "cheese", 50.5),
        ],
    )
    def test_get_name_returns_name(self, ingredient_type, name, price):
        """get_name возвращает название ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            ("SAUCE", "", 0),
            ("FILLING", "cheese", 50.5),
        ],
    )
    def test_get_type_returns_type(self, ingredient_type, name, price):
        """get_type возвращает тип ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
