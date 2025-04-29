from src.base_product import BaseProduct
from src.exceptions import AbsentPrice
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Нельзя добавить товар с нулевым количеством.")
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price*self.quantity + other.price*other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        else:
            self.__price = new_price

    @staticmethod
    def check_if_exists(new_name, new_quantity, new_price, existing_products):
        for product in existing_products:
            if new_name == product.name:
                product.quantity += new_quantity
                product.price = max(product.price, new_price)
        return existing_products

    @classmethod
    def new_product(cls, new_product):
        return cls(new_product['name'], new_product['description'], new_product['price'], new_product['quantity'])

    def sold(self):
        pass

class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        raise TypeError

    def sold(self):
        self.quantity = self.quantity - 1
        print(f"The product {self.name} was sold.")


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        raise TypeError

    def sold(self):
        self.quantity = self.quantity - 1
        print(f"The product {self.name} was sold.")

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        counter = 0
        for i in self.__products:
            counter += i.quantity
        return f'{self.name}, количество продуктов: {counter} шт.'


    @property
    def products(self):
        all_products = ''
        for product in self.__products:
            all_products += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return all_products

    @products.setter
    def products(self, new_product):
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise AbsentPrice("Нельзя добавить товар с нулевым количеством.")
            except AbsentPrice as e:
                print(str(e))
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                print("Товар успешно добавлен.")
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def avg_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0


smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180_000.0, 5, 44, 'Ultra', 128, 'black')
smartphone2 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 60_000.0, 7, 44, 'Ultra', 128, 'black')

category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [smartphone1, smartphone2]
    )
# print(category1.avg_price())

category2 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        []
    )
print(category2.avg_price())