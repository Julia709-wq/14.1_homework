import pytest
from src.classes import Product, Category


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
