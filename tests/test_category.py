from src.product import Product, Smartphone, LawnGrass
from src.category import Category

def test_category_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product])

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category._Category__products) == 1
    assert Category.category_count == 1
    assert Category.product_count == 1

def test_add_product():
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [])
    category.add_product(product)
    assert "Test Product, 100.0 руб. Остаток: 10 шт." in category.products

def test_private_products():
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product])
    assert hasattr(category, '_Category__products')

def test_category_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product])
    assert str(category) == "Test Category, количество продуктов: 10 шт."

def test_add_invalid_product():
    category = Category("Test Category", "Test Description", [])
    try:
        category.add_product("Not a product")
    except TypeError as e:
        assert str(e) == "Можно добавлять только объекты класса Product или его наследников"

def test_average_price():
    category = Category("Test Category", "Test Description")
    assert category.average_price() == 0

    product1 = Product("Test Product 1", "Test Description 1", 100.0, 10)
    product2 = Product("Test Product 2", "Test Description 2", 200.0, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == 150.0