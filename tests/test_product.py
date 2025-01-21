from src.product import Product

def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_price_setter():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = -50
    assert product.price == 100.0
    product.price = 150
    assert product.price == 150

def test_new_product():
    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 200.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 200.0
    assert product.quantity == 5