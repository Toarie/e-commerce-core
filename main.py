from src.product import Product
from src.category import Category

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Выводим информацию о продуктах
    print("Информация о продуктах:")
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создаем категорию и добавляем продукты
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    # Выводим информацию о категории
    print("\nИнформация о категории 'Смартфоны':")
    print(category1.name == "Смартфоны")
    print(category1.description)
    print("Количество продуктов в категории:", len(category1._Category__products))  # Доступ к приватному атрибуту
    print("Общее количество категорий:", Category.category_count)
    print("Общее количество продуктов:", Category.product_count)

    # Создаем новый продукт через класс-мет