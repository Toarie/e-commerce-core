from src.product import Product, Smartphone, LawnGrass

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

def test_product_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."

def test_product_add():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 5)
    assert product1 + product2 == 2000.0

def test_smartphone_initialization():
    smartphone = Smartphone("Smartphone", "Description", 500.0, 5, "High", "Model X", "128GB", "Black")
    assert smartphone.name == "Smartphone"
    assert smartphone.efficiency == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "128GB"
    assert smartphone.color == "Black"

def test_lawn_grass_initialization():
    lawn_grass = LawnGrass("Lawn Grass", "Description", 50.0, 20, "USA", "2 weeks", "Green")
    assert lawn_grass.name == "Lawn Grass"
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "2 weeks"
    assert lawn_grass.color == "Green"

def test_add_different_classes():
    product = Product("Product", "Description", 100.0, 10)
    smartphone = Smartphone("Smartphone", "Description", 500.0, 5, "High", "Model X", "128GB", "Black")
    try:
        product + smartphone
    except TypeError as e:
        assert str(e) == "Можно складывать только объекты одного класса"