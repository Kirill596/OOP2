class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price must be non‑negative")
        if quantity < 0:
            raise ValueError("Quantity must be non‑negative")
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "


class _ProductCollection:
    def __init__(self, products):
        self._products = products

    def __len__(self):
        return len(self._products)

    def __str__(self):
        return "".join(str(p) for p in self._products)

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        if isinstance(other, _ProductCollection):
            return self._products == other._products
        return False

    def __getattr__(self, item):
        return getattr(str(self), item)


class Category:
    all_category = 0
    all_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = list(products)
        Category.all_category += 1
        Category.all_product += len(self._products)

    @property
    def products(self):
        return _ProductCollection(self._products)

    def add_product(self, product):
        self._products.append(product)
        Category.all_product += 1

    def __str__(self):
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


# Let's run tests quickly
def setup_sample_category():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Смартфоны", "Смартфоны", [p1, p2, p3])


cat = setup_sample_category()
print(len(cat.products))
print(cat.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. Iphone 15, 210000.0 руб. Остаток: 8 шт. Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт. ")
