import pytest
from classes.Product import Product
from classes.Category import Category


@pytest.fixture
def product() -> "Product":
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product(product: Product) -> None:
    new_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    ret = product.new_product(new_dict)
    assert ret.name == "Samsung Galaxy S23 Ultra"


def test_price(product: Product) -> None:
    assert product.price == 180000.0
    product.price = 50
    assert product.price == 50
    product.price = -50
    assert product.price == 50


def test_product_str():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_product_add():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    assert product1 + product2 == 50000.0 * 10 + 100000.0 * 5


def test_product_add_type_error():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    with pytest.raises(TypeError):
        product + "Не продукт"


def test_product_price_setter_positive():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = 60000.0
    assert product.price == 60000.0


def test_product_price_setter_negative_or_zero():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = -1000.0
    assert product.price == 50000.0  # Проверяем, что цена не изменилась


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тест", "Тест", 100, 0)


def test_category_average_price():
    """Тест расчета средней цены категории"""
    # Случай с товарами
    p1 = Product("Товар 1", "Описание", 100, 10)
    p2 = Product("Товар 2", "Описание", 200, 5)
    cat = Category("Категория", "Описание", [p1, p2])
    assert cat.average_price() == 150.0

    # Случай без товаров
    empty_cat = Category("Пустая", "Описание", [])
    assert empty_cat.average_price() == 0

    # Случай с нулевой ценой
    p3 = Product("Товар 3", "Описание", 0, 1)
    cat_with_zero = Category("С нулем", "Описание", [p3])
    assert cat_with_zero.average_price() == 0


def test_add_product_with_zero_quantity():
    """Тест добавления продукта с нулевым количеством через new_product"""
    with pytest.raises(ValueError):
        Product.new_product({
            "name": "Тест",
            "description": "Тест",
            "price": 100,
            "quantity": 0
        })
