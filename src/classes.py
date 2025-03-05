class Product():
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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


class Category():
    name: str
    description: str
    products: list
    count_categories = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.count_categories += 1
        Category.count_products += len(products)

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
    def add_product(self, new_product):
        self.__products.append(new_product)
        self.count_products += 1

    @property
    def products_in_list(self):
        return self.__products




# category_1 = Category('name', 'description', [])
# category_1.add_product(Product('product_name', 'product_description', 14.45, 47))
# print(category_1.display_products)

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

product4 = Product.new_product({'name': 'Xiaomi Vacuum', 'description': 'робот-пылесос', 'price': 18000, 'quantity': 30})

summa = product1 + product2
# print(category1)
# print(product1)
# print(summa)