import pytest

from classes.Category import Category
from classes.Product import Product


@pytest.fixture
def category() -> "Category":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Смартфоны", "Смартфоны", [product1, product2, product3])


def test_init(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны"
    assert len(category.products) == 3
    assert category.all_category == 1
    assert category.all_product == 3


def test_products(category: Category) -> None:
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. Iphone 15, 210000.0 "
        "руб. Остаток: 8 шт. Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт. "
    )


def test_add_product(category: Category) -> None:
    all_product1 = category.all_product
    category.add_product(Product("Iphone 15", "512GB, Gray space", 210000.0, 8))
    assert all_product1 < category.all_product


def test_category_str():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])
    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_category_products_property():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])
    expected_output = "Телефон, 50000.0 руб. Остаток: 10 шт. Ноутбук, 100000.0 руб. Остаток: 5 шт. "
    assert category.products == expected_output


def test_category_add_product():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1])
    initial_product_count = Category.all_product
    category.add_product(product2)
    assert len(category.products.split()) == 24  # Проверяем, что добавился второй продукт
    assert Category.all_product == initial_product_count + 1


def test_category_counters():
    initial_category_count = Category.all_category
    initial_product_count = Category.all_product

    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    assert Category.all_category == initial_category_count + 1
    assert Category.all_product == initial_product_count + 2
