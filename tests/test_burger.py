import pytest
from unittest.mock import Mock
from constants import (
    REMOVE_CASES,
    MOVE_CASES,
    PRICE_CASES,
    RECEIPT_CASES,
)

class TestBurger:
    """Юнит-тесты для класса Burger."""

    # --- Базовые проверки инициализации ---
    def test_init_bun_is_none(self, burger_base):
        """При создании булочка не задана."""
        assert burger_base.bun is None

    def test_init_ingredients_is_empty_list(self, burger_base):
        """При создании список ингредиентов — пустой список."""
        assert burger_base.ingredients == []

    def test_init_ingredients_is_list_type(self, burger_base):
        """При создании ingredients имеет тип list."""
        assert isinstance(burger_base.ingredients, list)

    # --- set_buns ---
    def test_set_buns_assigns_bun(self, burger_base):
        """set_buns корректно устанавливает булочку."""
        mock_bun = Mock()
        burger_base.set_buns(mock_bun)
        assert burger_base.bun is mock_bun

    # --- add_ingredient ---
    def test_add_ingredient_increases_count(self, burger_base):
        """add_ingredient увеличивает длину списка ингредиентов."""
        mock_ingredient = Mock()
        burger_base.add_ingredient(mock_ingredient)
        assert len(burger_base.ingredients) == 1

    def test_add_ingredient_stores_reference(self, burger_base):
        """add_ingredient сохраняет ссылку на переданный ингредиент."""
        mock_ingredient = Mock()
        burger_base.add_ingredient(mock_ingredient)
        assert burger_base.ingredients[0] is mock_ingredient

    def test_add_ingredient_multiple_in_order(self, burger_base):
        """Несколько ингредиентов добавляются в порядке вызова."""
        first = Mock()
        second = Mock()
        third = Mock()
        burger_base.add_ingredient(first)
        burger_base.add_ingredient(second)
        burger_base.add_ingredient(third)
        assert burger_base.ingredients == [first, second, third]

    # --- remove_ingredient ---
    @pytest.mark.parametrize("add_count, remove_index, expected_length", REMOVE_CASES)
    def test_remove_ingredient_by_index(self, burger_base, add_count, remove_index, expected_length):
        """remove_ingredient удаляет ингредиент по индексу и обновляет длину списка."""
        for _ in range(add_count):
            burger_base.add_ingredient(Mock())
        burger_base.remove_ingredient(remove_index)
        assert len(burger_base.ingredients) == expected_length

    # --- move_ingredient ---
    @pytest.mark.parametrize("old_index, new_index, expected_order", MOVE_CASES)
    def test_move_ingredient_changes_order(
        self, burger_base, old_index, new_index, expected_order
    ):
        """move_ingredient корректно меняет порядок элементов в списке."""
        ingredients = [Mock(), Mock(), Mock()]
        for ing in ingredients:
            burger_base.add_ingredient(ing)
        burger_base.move_ingredient(old_index, new_index)

        # Переводим реальные объекты в индексы, чтобы сравнить порядок
        actual_order = [ingredients.index(ing) for ing in burger_base.ingredients]
        assert actual_order == expected_order

    # --- get_price ---
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", PRICE_CASES)
    def test_get_price_calculation(self, burger_base, bun_price, ingredient_prices, expected_total):
        """get_price корректно считает итоговую цену бургера."""
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger_base.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger_base.add_ingredient(mock_ing)

        assert burger_base.get_price() == expected_total

    # --- get_receipt (полный чек) ---
    @pytest.mark.parametrize("case", RECEIPT_CASES, ids=[c["id"] for c in RECEIPT_CASES])
    def test_get_receipt_full(self, burger_base, case):
        """get_receipt возвращает чек в ожидаемом формате (полное совпадение строки)."""
        # Булочка
        mock_bun = Mock()
        mock_bun.get_name.return_value = case["bun_name"]
        mock_bun.get_price.return_value = case["bun_price"]
        burger_base.set_buns(mock_bun)

        # Ингредиенты
        for ing_data in case["ingredients"]:
            mock_ing = Mock()
            mock_ing.get_type.return_value = ing_data["type"]
            mock_ing.get_name.return_value = ing_data["name"]
            mock_ing.get_price.return_value = ing_data["price"]
            burger_base.add_ingredient(mock_ing)

        receipt = burger_base.get_receipt()
        assert receipt == case["expected_receipt"]