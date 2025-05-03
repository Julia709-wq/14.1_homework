import pytest

from src.classes import Category, Product, Smartphone
from tests.conftest import first_product, first_category, lawngrass1


def test_products_init(first_product, second_product):
    """Тест инициализации продуктов"""
    assert first_product.name == 'KitKat'
    assert first_product.description == 'Шоколадный батончик'
    assert first_product.price == 59.99
    assert first_product.quantity == 140

    assert second_product.name == 'Fanta'
    assert second_product.description == 'Газированный напиток'
    assert second_product.price == 89.99
    assert second_product.quantity == 350


def test_categories_init(first_category, second_category):
    """Тест инициализации категорий"""
    assert first_category.name == 'Напитки'
    assert first_category.description == 'Все напитки'

    assert second_category.name == 'Корм для животных'
    assert second_category.description == 'Для кошек'


def test_count_categories(first_category, second_category):
    assert Category.category_count == 6


def test_count_products(first_category, second_category):
    assert Category.product_count == 11


def test_read_json(tmp_path):
    test_data = '[{"name": "Категория", "description": "Тест", "products": []}]'
    test_file = tmp_path / "data.json"
    test_file.write_text(test_data, encoding='utf-8')

    from src.read_json import read_json
    result = read_json(str(test_file))
    assert isinstance(result, list)
    assert result[0]['name'] == "Категория"


def test_create_objects_from_json():
    from src.read_json import create_objects_from_json
    from src.classes import Category

    test_data = [
        {
            "name": "Категория",
            "description": "Описание",
            "products": [
                {"name": "Товар", "description": "Описание товара", "price": 100, "quantity": 5}
            ]
        }
    ]
    result = create_objects_from_json(test_data)
    assert isinstance(result[0], Category)
    assert result[0].products_in_list[0].name == "Товар"


# тест класс-метода new_product
def test_new_product_created():
    data = {
        'name': 'Xiaomi Vacuum',
        'description': 'робот-пылесос',
        'price': 18000,
        'quantity': 30
    }
    product = Product.new_product(data)
    assert product.name == 'Xiaomi Vacuum'
    assert product.description == 'робот-пылесос'
    assert product.price == 18000
    assert product.quantity == 30

def test_product_price_getter():
    product = Product("Test", "Test description", 999.99, 10)
    assert product.price == 999.99

# тесты сеттера новой цены
def test_price_setter(capsys, first_product):
    first_product.price = 100
    assert first_product.price == 100

def test_price_setter_negative_price(capsys, first_product):
    first_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Цена не должна быть нулевая или отрицательная'


# тест для геттера списка продуктов
def test_category_products_getter():
    product = Product("Phone", "Смартфон", 15000, 3)
    category = Category("Электроника", "Смартфоны", [])
    category.products = product

    result = category.products
    expected = "Phone, 15000 руб. Остаток: 3 шт.\n"
    assert result == expected


# тест для проверки добавления нового продукта в список
def test_products_list_setter(first_category, new_product):
    assert len(first_category.products_in_list) == 2
    first_category.products = new_product
    assert len(first_category.products_in_list) == 3

def test_category_products_empty():
    empty_category = Category("Пустая категория", "Нет товаров", [])
    assert empty_category.products == ''


def test_check_if_exists(first_product):
    existing = [first_product]
    Product.check_if_exists("KitKat", 10, 50, existing)
    assert first_product.quantity == 150
    assert first_product.price == 59.99

    Product.check_if_exists("KitKat", 10, 100, existing)
    assert first_product.price == 100

def test_category_products_in_list():
    p1 = Product("Product1", "Desc", 100, 5)
    p2 = Product("Product2", "Desc", 200, 3)
    category = Category("Тестовая", "Описание", [p1, p2])
    result = category.products_in_list
    assert isinstance(result, list)
    assert p1 in result
    assert p2 in result
    assert len(result) == 2


# тест для магического метода __str__ класса Product
def test_str_product(first_product):
    expected_output = 'KitKat, 59.99 руб. Остаток: 140 шт.'
    assert str(first_product) == expected_output

# тест для магического метода __str__ класса Category
def test_str_category(first_category):
    expected_output = 'Напитки, количество продуктов: 587 шт.'
    assert str(first_category) == expected_output

def test_category_str_with_no_products():
    category = Category('Пустая', 'Категория без товаров', [])
    assert str(category) == 'Пустая, количество продуктов: 0 шт.'

def test_category_add_product_with_zero_quantity(first_category, capsys):
    zero_product = Product("Test", "Desc", 100, 1)
    zero_product.quantity = 0  # вручную, чтобы обойти ValueError конструктора

    first_category.products = zero_product
    output = capsys.readouterr().out.strip()
    assert "Нельзя добавить товар с нулевым количеством." in output

# тест для магического метода __add__ класса Product
def test_add_product(first_product, second_product):
    expected_result = 59.99*140 + 89.99*350
    assert first_product.__add__(second_product) == expected_result

# тест для проверки возникновения ошибки при попытке добавить в список товаров объект не класса Product
def test_products_list_setter_error(first_category, new_product):
    with pytest.raises(TypeError):
        first_category.products = 1

def test_products_list_setter_smartphone(first_category, smartphone1):
    first_category.products = smartphone1
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
    assert (smartphone2 + smartphone1) == 570

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

def test_smartphone_sold(smartphone1, capsys):
    initial_quantity = smartphone1.quantity
    smartphone1.sold()
    assert smartphone1.quantity == initial_quantity - 1
    output = capsys.readouterr().out.strip()
    assert f"The product {smartphone1.name} was sold." in output

def test_lawngrass_add(lawngrass1, lawngrass2):
    assert (lawngrass2 + lawngrass1) == 828

def test_lawngrass_add_error(lawngrass1, lawngrass2):
    with pytest.raises(TypeError):
        result = lawngrass1 + 1

def test_smartphone_add_invalid_type():
    phone = Smartphone("iPhone", "desc", 100000, 10, "высокая", "15 Pro", "512", "серый")
    with pytest.raises(TypeError):
        result = phone + "NotASmartphone"


def test_lawngrass_sold(lawngrass1, capsys):
    initial_quantity = lawngrass1.quantity
    lawngrass1.sold()
    assert lawngrass1.quantity == initial_quantity - 1
    output = capsys.readouterr().out.strip()
    assert f"The product {lawngrass1.name} was sold." in output

def test_avg_price(category_without_products, first_category):
    assert category_without_products.avg_price() == 0
    assert first_category.avg_price() == 60

def test_avg_price_with_one_product(second_category):
    assert second_category.avg_price() == 56.99

def test_category_avg_price_zero_division():
    empty_category = Category("Empty", "No products", [])
    assert empty_category.avg_price() == 0

def test_custom_exception(capsys, first_category):
    assert len(first_category.products_in_list) == 2
    product_add = Product('Fanta', 'Газированный напиток', 90, 10)
    first_category.products = product_add
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Товар успешно добавлен."

def test_product_zero_quantity_raises_value_error():
    with pytest.raises(ValueError) as exc_info:
        Product("Test Product", "Description", 100.0, 0)
    assert str(exc_info.value) == "Нельзя добавить товар с нулевым количеством."

def test_absent_price_exception():
    from src.exceptions import AbsentPrice
    with pytest.raises(AbsentPrice):
        raise AbsentPrice("Ошибка с ценой")

def test_category_products_setter_raises_absent_price(capsys):
    category = Category("Тест", "Пустая категория", [])
    product = Product("ZeroProduct", "Без количества", 100, 1)
    product.quantity = 0  # обнуляем quantity вручную

    category.products = product
    output = capsys.readouterr().out.strip()
    assert "Нельзя добавить товар с нулевым количеством." in output
    assert len(category.products_in_list) == 0