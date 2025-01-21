from src.product import Product

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []  # Приватный атрибут

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])