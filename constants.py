# constants.py
# Все тестовые данные для юнит-тестов Stellar Burgers

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# --- Данные для теста Bun ---
BUN_CASES = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
    ("", 0),
    ("флюоресцентная булка", 988.0),
]

BUN_NAME_CASES = BUN_CASES  # можно использовать тот же список, если нужны только name/price
BUN_PRICE_CASES = BUN_CASES


# --- Данные для теста Burger: remove_ingredient ---
REMOVE_CASES = [
    (1, 0, 0),   # add_count, remove_index, expected_length
    (3, 0, 2),
    (3, 1, 2),
    (3, 2, 2),
    (5, 3, 4),
]


# --- Данные для теста Burger: move_ingredient ---
# old_index, new_index, ожидаемый порядок индексов (для проверки)
MOVE_CASES = [
    (0, 1, [1, 0, 2]),
    (0, 2, [1, 2, 0]),
    (1, 0, [1, 0, 2]),
    (1, 2, [0, 2, 1]),
    (2, 0, [2, 0, 1]),
    (2, 1, [0, 2, 1]),
]


# --- Данные для теста Burger: get_price ---
PRICE_CASES = [
    (0, [], 0),
    (100, [], 200),
    (100, [50], 250),
    (100, [50, 50, 50], 350),
    (200, [100, 200, 300], 1000),
    (0, [10, 20, 30], 60),
    (150, [25, 35], 360),
]


# --- Данные для теста Burger: get_receipt (полный чек) ---
# Каждый кейс — словарь, чтобы хранить bun, ингредиенты и ожидаемый чек целиком
RECEIPT_CASES = [
    {
        "id": "only_bun_black",
        "bun_name": "black bun",
        "bun_price": 100,
        "ingredients": [],
        "expected_receipt": "(==== black bun ====)\n(==== black bun ====)\n\nPrice: 200",
    },
    {
        "id": "bun_plus_sauce",
        "bun_name": "red bun",
        "bun_price": 300,
        "ingredients": [
            {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100}
        ],
        "expected_receipt": (
            "(==== red bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== red bun ====)\n"
            "\n"
            "Price: 700"
        ),
    },
    {
        "id": "bun_plus_filling",
        "bun_name": "white bun",
        "bun_price": 200,
        "ingredients": [
            {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        ],
        "expected_receipt": (
            "(==== white bun ====)\n"
            "= filling cutlet =\n"
            "(==== white bun ====)\n"
            "\n"
            "Price: 500"
        ),
    },
    {
        "id": "multiple_ingredients",
        "bun_name": "black bun",
        "bun_price": 100,
        "ingredients": [
            {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
            {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
            {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
        ],
        "expected_receipt": (
            "(==== black bun ====)\n"
            "= filling sausage =\n"
            "= filling dinosaur =\n"
            "= sauce sour cream =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 900"
        ),
    },
]


# --- Данные для теста Database ---
BUN_DB_CASES = [
    (0, "black bun", 100),
    (1, "white bun", 200),
    (2, "red bun", 300),
]

INGREDIENT_DB_CASES = [
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
]


# --- Данные для теста Ingredient ---
INGREDIENT_INIT_CASES = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ("SAUCE", "", 0),
    ("FILLING", "cheese", 50.5),
]

INGREDIENT_GETTER_CASES = INGREDIENT_INIT_CASES
