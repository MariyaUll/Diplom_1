import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from constants import BUN_DB_CASES, INGREDIENT_DB_CASES


class TestDatabase:
    """Юнит-тесты для класса Database."""

    # --- Базовые проверки структуры ---
    def test_buns_is_list(self, db_context):
        """При инициализации buns — это список."""
        assert isinstance(db_context["db"].buns, list)

    def test_buns_count(self, db_context):
        """В базе ровно 3 булочки."""
        assert len(db_context["buns"]) == 3

    def test_ingredients_is_list(self, db_context):
        """При инициализации ingredients — это список."""
        assert isinstance(db_context["db"].ingredients, list)

    def test_ingredients_count(self, db_context):
        """В базе ровно 6 ингредиентов."""
        assert len(db_context["ingredients"]) == 6

    # --- Тесты булочек ---
    @pytest.mark.parametrize("index", [case[0] for case in BUN_DB_CASES])
    def test_available_buns_returns_bun_instance(self, db_context, index):
        """available_buns возвращает экземпляр Bun."""
        assert isinstance(db_context["buns"][index], Bun)

    @pytest.mark.parametrize("index, expected_name", [(case[0], case[1]) for case in BUN_DB_CASES])
    def test_available_buns_returns_correct_name(self, db_context, index, expected_name):
        """available_buns возвращает булочки с корректными названиями."""
        assert db_context["buns"][index].get_name() == expected_name

    @pytest.mark.parametrize("index, expected_price", [(case[0], case[2]) for case in BUN_DB_CASES])
    def test_available_buns_returns_correct_price(self, db_context, index, expected_price):
        """available_buns возвращает булочки с корректными ценами."""
        assert db_context["buns"][index].get_price() == expected_price

    # --- Тесты ингредиентов ---
    @pytest.mark.parametrize("index", [case[0] for case in INGREDIENT_DB_CASES])
    def test_available_ingredients_returns_ingredient_instance(
        self, db_context, index
    ):
        """available_ingredients возвращает экземпляр Ingredient."""
        assert isinstance(db_context["ingredients"][index], Ingredient)

    @pytest.mark.parametrize(
        "index, expected_type", [(case[0], case[1]) for case in INGREDIENT_DB_CASES]
    )
    def test_available_ingredients_returns_correct_type(
        self, db_context, index, expected_type
    ):
        """available_ingredients возвращает ингредиенты с корректными типами."""
        assert db_context["ingredients"][index].get_type() == expected_type

    @pytest.mark.parametrize(
        "index, expected_name", [(case[0], case[2]) for case in INGREDIENT_DB_CASES]
    )
    def test_available_ingredients_returns_correct_name(
        self, db_context, index, expected_name
    ):
        """available_ingredients возвращает ингредиенты с корректными названиями."""
        assert db_context["ingredients"][index].get_name() == expected_name

    @pytest.mark.parametrize(
        "index, expected_price", [(case[0], case[3]) for case in INGREDIENT_DB_CASES]
    )
    def test_available_ingredients_returns_correct_price(
        self, db_context, index, expected_price
    ):
        """available_ingredients возвращает ингредиенты с корректными ценами."""
        assert db_context["ingredients"][index].get_price() == expected_price
