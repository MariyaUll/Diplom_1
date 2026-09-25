import pytest

from praktikum.bun import Bun


class TestBun:
    """Юнит-тесты для класса Bun."""

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("", 0),
            ("флюоресцентная булка", 988.0),
        ],
    )
    def test_init_bun_attributes(self, name, price):
        """Конструктор корректно сохраняет название и цену."""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("", 0),
            ("custom bun", 99.99),
        ],
    )
    def test_get_name_returns_name(self, name, price):
        """get_name возвращает название булочки."""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("", 0),
            ("custom bun", 99.99),
        ],
    )
    def test_get_price_returns_price(self, name, price):
        """get_price возвращает цену булочки."""
        bun = Bun(name, price)
        assert bun.get_price() == price
