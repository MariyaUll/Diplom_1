import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from constants import (
    BUN_CASES,
    INGREDIENT_INIT_CASES,
)

@pytest.fixture(scope="class")
def db_context():
    """Контекст для Database: экземпляр БД и готовые списки buns/ingredients."""
    db = Database()
    return {
        "db": db,
        "buns": db.available_buns(),
        "ingredients": db.available_ingredients(),
    }

@pytest.fixture(scope="class")
def bun_cases():
    """Готовые объекты Bun для продвинутых сценариев (не используется в параметризации)."""
    cases = []
    for name, price in BUN_CASES:
        bun = Bun(name, price)
        cases.append((bun, name, price))
    return cases

@pytest.fixture
def burger_base():
    """Базовый экземпляр Burger (без булочек и ингредиентов) для тестов."""
    from praktikum.burger import Burger
    return Burger()