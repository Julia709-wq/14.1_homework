import pytest
from src.classes import Product, Category, Smartphone, LawnGrass


@pytest.fixture(autouse=True)
def reset_counters():
    Category.count_categories = 0
    Category.count_products = 0


@pytest.fixture
def first_product(scope='function'):
    return Product(
        'KitKat', 'Шоколадный батончик', 59.99, 140
    )


@pytest.fixture
def second_product():
    return Product(
        'Fanta', 'Газированный напиток', 89.99, 350
    )


@pytest.fixture
def first_category(scope='function'):
    return Category(
        'Напитки', 'Все напитки', [
            Product('Fanta', 'Газированный напиток', 89.99, 350),
            Product('Saint Spring', 'Негазированная вода', 39.99, 237)]
    )


@pytest.fixture
def second_category(scope='function'):
    return Category(
        'Корм для животных', 'Для кошек', [
            Product('Whiskas', 'Сухой корм', 56.99, 415)]
    )

@pytest.fixture
def new_product(scope='function'):
    return Product(
        'BigBon', 'Продукт быстрого приготовления', 49.99, 398
    )

@pytest.fixture
def smartphone1():
    return Smartphone("Смартфон", "Последний ипхон", 90_000, 395,
                      "очень хорошая", "16 Pro", "256", "Blue")

@pytest.fixture
def smartphone2():
    return Smartphone("Смартфон", "Предпоследний ипхон", 70_000, 175,
                      "хорошая", "15 Pro", "256", "Pink")

@pytest.fixture
def lawngrass1():
    return LawnGrass("Трава для газона", "красивая", 10_000, 314,
                     "China", "10 days", "ярко-зеленый")

@pytest.fixture
def lawngrass2():
    return LawnGrass("Трава для газона", "красивая", 6_000, 514,
                     "China", "14 days", "бирюзовый")

