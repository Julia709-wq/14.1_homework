import json
import os
from src.classes import Product, Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    products = []
    for product in data:
        list_products = []
        for p in product['products']:
            list_products.append(Product(**p))
        product['products'] = list_products
        products.append(Category(**product))
    return products


if __name__ == '__main__':
    raw_data = read_json('../data/products.json')
    categories_data = create_objects_from_json(raw_data)
    print(categories_data[0].name)
    print(categories_data[0].description)
    print(categories_data[0].products)
