import pytest
from praktikum.bun import Bun
from constants import BUN_CASES

class TestBun:
    """Юнит-тесты для класса Bun."""

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_init_creates_instance(self, name, price):
        """Конструктор создаёт корректный экземпляр Bun."""
        bun = Bun(name, price)
        assert isinstance(bun, Bun)

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_init_saves_name(self, name, price):
        """Конструктор корректно сохраняет название."""
        bun = Bun(name, price)
        assert bun.name == name

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_init_saves_price(self, name, price):
        """Конструктор корректно сохраняет цену."""
        bun = Bun(name, price)
        assert bun.price == price

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_name_returns_name(self, name, price):
        """get_name возвращает сохранённое название."""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_price_returns_price(self, name, price):
        """get_price возвращает сохранённую цену."""
        bun = Bun(name, price)
        assert bun.get_price() == price