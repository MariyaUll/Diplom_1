import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestBurger:
    """Юнит-тесты для класса Burger."""

    # ── Тесты __init__ ──────────────────────────────────────────────

    def test_init_bun_is_none(self):
        """При создании бургера булочка не задана."""
        burger = Burger()
        assert burger.bun is None

    def test_init_ingredients_is_empty_list(self):
        """При создании бургера список ингредиентов пуст."""
        burger = Burger()
        assert burger.ingredients == []
        assert isinstance(burger.ingredients, list)

    # ── Тесты set_buns ─────────────────────────────────────────────

    def test_set_buns_assigns_bun(self):
        """set_buns корректно устанавливает булочку."""
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    # ── Тесты add_ingredient ────────────────────────────────────────

    def test_add_ingredient_appends_to_list(self):
        """add_ingredient добавляет ингредиент в конец списка."""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is mock_ingredient

    def test_add_ingredient_multiple_appends_in_order(self):
        """Несколько ингредиентов добавляются в порядке вызова."""
        burger = Burger()
        first = Mock()
        second = Mock()
        third = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)
        assert burger.ingredients == [first, second, third]

    # ── Тесты remove_ingredient ────────────────────────────────────

    def test_remove_ingredient_removes_by_index(self):
        """remove_ingredient удаляет ингредиент по индексу."""
        burger = Burger()
        mock_1 = Mock()
        mock_2 = Mock()
        mock_3 = Mock()
        burger.add_ingredient(mock_1)
        burger.add_ingredient(mock_2)
        burger.add_ingredient(mock_3)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_1, mock_3]
        assert len(burger.ingredients) == 2

    @pytest.mark.parametrize(
        "add_count, remove_index, expected_length",
        [
            (1, 0, 0),
            (3, 0, 2),
            (3, 1, 2),
            (3, 2, 2),
            (5, 3, 4),
        ],
    )
    def test_remove_ingredient_parametrized(
        self, add_count, remove_index, expected_length
    ):
        """Параметризованная проверка удаления по разным индексам."""
        burger = Burger()
        for i in range(add_count):
            burger.add_ingredient(Mock())
        burger.remove_ingredient(remove_index)
        assert len(burger.ingredients) == expected_length

    # ── Тесты move_ingredient ──────────────────────────────────────

    def test_move_ingredient_moves_from_end_to_start(self):
        """Перемещение ингредиента с последней позиции в начало."""
        burger = Burger()
        first, second, third = Mock(), Mock(), Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [third, first, second]

    def test_move_ingredient_moves_from_start_to_end(self):
        """Перемещение ингредиента с первой позиции в конец."""
        burger = Burger()
        first, second, third = Mock(), Mock(), Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [second, third, first]

    @pytest.mark.parametrize(
        "old_index, new_index, expected_order",
        [
            (0, 1, [1, 0, 2]),
            (0, 2, [1, 2, 0]),
            (1, 0, [1, 0, 2]),
            (1, 2, [0, 2, 1]),
            (2, 0, [2, 0, 1]),
            (2, 1, [0, 2, 1]),
        ],
    )
    def test_move_ingredient_parametrized(self, old_index, new_index, expected_order):
        """Параметризованная проверка перемещения ингредиентов."""
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]
        for ing in ingredients:
            burger.add_ingredient(ing)
        burger.move_ingredient(old_index, new_index)
        actual_order = [ingredients.index(ing) for ing in burger.ingredients]
        assert actual_order == expected_order

    # ── Тесты get_price ─────────────────────────────────────────────

    def test_get_price_only_bun(self):
        """Цена бургера без ингредиентов = цена булочки x 2."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200

    def test_get_price_bun_and_ingredients(self):
        """Цена бургера = булочка x 2 + сумма ингредиентов."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ing_1 = Mock()
        mock_ing_1.get_price.return_value = 50
        mock_ing_2 = Mock()
        mock_ing_2.get_price.return_value = 75
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        assert burger.get_price() == 325

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        [
            (0, [], 0),
            (100, [], 200),
            (100, [50], 250),
            (100, [50, 50, 50], 350),
            (200, [100, 200, 300], 1000),
            (0, [10, 20, 30], 60),
            (150, [25, 35], 360),
        ],
    )
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected_total):
        """Параметризованная проверка расчёта цены."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_total

    # ── Тесты get_receipt ──────────────────────────────────────────

    def test_get_receipt_structure(self):
        """Чек содержит булочку сверху и снизу, ингредиенты и цену."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_sauce = Mock()
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        mock_sauce.get_price.return_value = 100
        burger.add_ingredient(mock_sauce)

        mock_filling = Mock()
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 100
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400"
        )
        assert receipt == expected

    def test_get_receipt_only_bun(self):
        """Чек с одной булочкой без ингредиентов."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        expected = "(==== white bun ====)\n" "(==== white bun ====)\n" "\n" "Price: 400"
        assert receipt == expected

    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredients_data, expected_price",
        [
            ("black bun", 100, [], 200),
            ("red bun", 300, [("SAUCE", "hot sauce", 100)], 700),
            (
                "white bun",
                200,
                [
                    ("SAUCE", "chili sauce", 300),
                    ("FILLING", "cutlet", 100),
                ],
                800,
            ),
            (
                "black bun",
                100,
                [
                    ("FILLING", "sausage", 300),
                    ("FILLING", "dinosaur", 200),
                    ("SAUCE", "sour cream", 200),
                ],
                900,
            ),
        ],
    )
    def test_get_receipt_parametrized(
        self, bun_name, bun_price, ingredients_data, expected_price
    ):
        """Параметризованная проверка формирования чека."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for ing_type, ing_name, ing_price in ingredients_data:
            mock_ing = Mock()
            mock_ing.get_type.return_value = ing_type
            mock_ing.get_name.return_value = ing_name
            mock_ing.get_price.return_value = ing_price
            burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()

        assert f"(==== {bun_name} ====)" in receipt
        assert f"Price: {expected_price}" in receipt
        for ing_type, ing_name, ing_price in ingredients_data:
            assert f"= {ing_type.lower()} {ing_name} =" in receipt

    def test_get_receipt_calls_get_price(self):
        """get_receipt вызывает get_price для расчёта итоговой суммы."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        mock_ing = Mock()
        mock_ing.get_type.return_value = "SAUCE"
        mock_ing.get_name.return_value = "test sauce"
        mock_ing.get_price.return_value = 25
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        assert "Price: 125" in receipt

    def test_get_receipt_type_lowercased(self):
        """Тип ингредиента в чеке приводится к нижнему регистру."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ing = Mock()
        mock_ing.get_type.return_value = "FILLING"
        mock_ing.get_name.return_value = "cheese"
        mock_ing.get_price.return_value = 50
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        assert "= filling cheese =" in receipt
