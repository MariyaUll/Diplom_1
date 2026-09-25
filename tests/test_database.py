import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestDatabase:
    """Юнит-тесты для класса Database."""

    def test_init_creates_buns_list(self):
        """При создании Database список булочек инициализирован."""
        db = Database()
        assert isinstance(db.buns, list)
        assert len(db.buns) == 3

    def test_init_creates_ingredients_list(self):
        """При создании Database список ингредиентов инициализирован."""
        db = Database()
        assert isinstance(db.ingredients, list)
        assert len(db.ingredients) == 6

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
    )
    def test_available_buns_returns_correct_buns(
        self, index, expected_name, expected_price
    ):
        """available_buns возвращает список с корректными булочками."""
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns[index], Bun)
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
    )
    def test_available_ingredients_returns_correct_ingredients(
        self, index, expected_type, expected_name, expected_price
    ):
        """available_ingredients возвращает список с корректными ингредиентами."""
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients[index], Ingredient)
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price

    def test_available_buns_returns_list(self):
        """available_buns возвращает список."""
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3

    def test_available_ingredients_returns_list(self):
        """available_ingredients возвращает список."""
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
