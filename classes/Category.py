from classes.Product import Product


class Category:
    """содержит описание категории"""

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
        self.__products = products

        Category.all_category += 1
        Category.all_product += len(products)

    @property
    def products(self) -> str:
        count = ""
        for i in self.__products:
            count += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт. "
        return count

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.all_product += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

