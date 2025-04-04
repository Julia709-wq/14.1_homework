import pytest
from src.classes import Category, Product, Smartphone
from tests.conftest import first_product, first_category, lawngrass1


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


# тест класс-метода new_product
def test_new_product_created():
    product = Product('Xiaomi Vacuum', 'робот-пылесос', 18000, 30)
    assert product.name == 'Xiaomi Vacuum'
    assert product.description == 'робот-пылесос'
    assert product.price == 18000
    assert product.quantity == 30


# тест сеттера новой цены
def test_price_setter(capsys, first_product):
    first_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'

    first_product.price = 100
    assert first_product.price == 100


# тест для геттера списка продуктов
def test_products_list_property(first_category):
    assert first_category.products == ('Fanta, 89.99 руб. Остаток: 350 шт.\n'
                                        'Saint Spring, 39.99 руб. Остаток: 237 шт.\n')


# тест для проверки добавления нового продукта в список
def test_products_list_setter(first_category, new_product):
    assert len(first_category.products_in_list) == 2
    first_category.add_product = new_product
    assert len(first_category.products_in_list) == 3


# тест для магического метода __str__ класса Product
def test_str_product(first_product):
    expected_output = 'KitKat, 59.99 руб. Остаток: 140 шт.'
    assert str(first_product) == expected_output


# тест для магического метода __str__ класса Category
def test_str_category(first_category):
    expected_output = 'Напитки, количество продуктов: 587 шт.'
    assert str(first_category) == expected_output


# тест для магического метода __add__ класса Product
def test_add_product(first_product, second_product):
    expected_result = 59.99*140 + 89.99*350
    assert first_product.__add__(second_product) == expected_result


# тест для проверки возникновения ошибки при попытке добавить в список товаров объект не класса Product
def test_products_list_setter_error(first_category, new_product):
    with pytest.raises(TypeError):
        first_category.add_product = 1

def test_products_list_setter_smartphone(first_category, smartphone1):
    first_category.add_product = smartphone1
    assert first_category.products_in_list[-1].name == 'Смартфон'

def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Смартфон"
    assert smartphone1.description == "Последний ипхон"
    assert smartphone1.price == 90_000
    assert smartphone1.quantity == 395
    assert smartphone1.efficiency == "очень хорошая"
    assert smartphone1.model == "16 Pro"
    assert smartphone1.memory == "256"
    assert smartphone1.color == "Blue"

def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone2.quantity + smartphone1.quantity == 570

def test_smartphone_add_error(smartphone1, smartphone2):
    with pytest.raises(TypeError):
        result = smartphone1 + 1

def test_lawn_grass1_init(lawngrass1):
    assert lawngrass1.name == "Трава для газона"
    assert lawngrass1.description == "красивая"
    assert lawngrass1.price == 10_000
    assert lawngrass1.quantity == 314
    assert lawngrass1.country == "China"
    assert lawngrass1.germination_period == "10 days"
    assert lawngrass1.color == "ярко-зеленый"

def test_lawn_grass2_init(lawngrass2):
    assert lawngrass2.name == "Трава для газона"
    assert lawngrass2.description == "красивая"
    assert lawngrass2.price == 6_000
    assert lawngrass2.quantity == 514
    assert lawngrass2.country == "China"
    assert lawngrass2.germination_period == "14 days"
    assert lawngrass2.color == "бирюзовый"

def test_lawngrass_add(lawngrass1, lawngrass2):
    assert lawngrass2.quantity + lawngrass1.quantity == 828

def test_lawngrass_add_error(lawngrass1, lawngrass2):
    with pytest.raises(TypeError):
        result = lawngrass1 + 1
