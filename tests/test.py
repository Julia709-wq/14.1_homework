from src.classes import Category


def test_products_init(first_product, second_product):
    assert first_product.name == 'KitKat'
    assert first_product.description == 'Шоколадный батончик'
    assert first_product.price == 59.99
    assert first_product.quantity == 140

    assert second_product.name == 'Fanta'
    assert second_product.description == 'Газированный напиток'
    assert second_product.price == 89.99
    assert second_product.quantity == 350


def test_categories_init(first_category, second_category):
    assert first_category.name == 'Напитки'
    assert first_category.description == 'Все напитки'

    assert second_category.name == 'Корм для животных'
    assert second_category.description == 'Для кошек'


def test_count_categories(first_category, second_category):
    assert Category.count_categories == 2


def test_count_products(first_category, second_category):
    assert Category.count_products == 3
