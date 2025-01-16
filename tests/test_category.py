from src.product import Product
from src.category import Category

def test_category_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product])

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 1
    assert Category.category_count == 1
    assert Category.product_count == 1