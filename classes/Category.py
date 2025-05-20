from classes.Product import Product


class Category:
    """Класс категории товаров"""

    name: str
    description: str
    __products: list
    all_category: int
    all_product: int

    all_category = 0
    all_product = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = []

        for product in products:
            self.add_product(product)

        Category.all_category += 1

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.all_product += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self) -> float:
        """Метод расчета средней цены товаров в категории"""
        if not self.__products:
            return 0

        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0
