from src.product import Product
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