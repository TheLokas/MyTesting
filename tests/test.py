
import unittest
from main import Product, Order  # Предполагается, что основной код находится в файле app.py

class TestProduct(unittest.TestCase):
    # Блочные тесты для класса Product

    def setUp(self):
        # Настройка начальных данных перед каждым тестом
        self.product = Product("Laptop", 1500.0, 10)

    def test_get_name(self):
        # Тест получения имени продукта
        self.assertEqual(self.product.get_name(), "Laptop")

    def test_get_price(self):
        # Тест получения цены продукта
        self.assertEqual(self.product.get_price(), 1500.0)

    def test_update_stock_success(self):
        # Тест успешного уменьшения количества товара на складе
        self.assertTrue(self.product._update_stock(5))
        self.assertEqual(self.product.get_stock_quantity(), 5)

    def test_update_stock_failure(self):
        # Тест неудачного уменьшения количества товара на складе, если его недостаточно
        self.assertFalse(self.product._update_stock(15))
        self.assertEqual(self.product.get_stock_quantity(), 10)


class TestOrder(unittest.TestCase):
    # Блочные тесты для класса Order

    def setUp(self):
        # Настройка начальных данных перед каждым тестом
        self.product1 = Product("Laptop", 1500.0, 10)
        self.product2 = Product("Smartphone", 800.0, 5)
        self.order = Order()

    def test_add_product_success(self):
        # Тест успешного добавления товара в заказ
        self.order.add_product(self.product1, 2)
        self.assertEqual(self.order.get_total_cost(), 3000.0)
        self.assertEqual(self.product1.get_stock_quantity(), 8)

    def test_add_product_failure(self):
        # Тест неудачного добавления товара в заказ, если его недостаточно на складе
        self.order.add_product(self.product2, 6)
        self.assertEqual(self.order.get_total_cost(), 0)
        self.assertEqual(self.product2.get_stock_quantity(), 5)

    def test_update_status(self):
        # Тест обновления статуса заказа
        self.order.update_status("Shipped")
        self.assertEqual(self.order.get_status(), "Shipped")


class TestIntegration(unittest.TestCase):
    # Интеграционные тесты для взаимодействия классов Product и Order

    def setUp(self):
        # Настройка начальных данных перед каждым тестом
        self.product1 = Product("Laptop", 1500.0, 10)
        self.product2 = Product("Smartphone", 500.0, 5)
        self.order = Order()

    def test_order_with_multiple_products(self):
        # Тест заказа с несколькими товарами
        self.order.add_product(self.product1, 2)  # Добавляем 2 ноутбука
        self.order.add_product(self.product2, 3)  # Добавляем 3 смартфона
        self.assertEqual(self.order.get_total_cost(), 4500.0)
        self.assertEqual(self.product1.get_stock_quantity(), 8)
        self.assertEqual(self.product2.get_stock_quantity(), 2)

    def test_order_status_flow(self):
        # Тест изменения статуса заказа от "Pending" к "Shipped"
        self.assertEqual(self.order.get_status(), "Pending")
        self.order.update_status("Processing")
        self.assertEqual(self.order.get_status(), "Processing")
        self.order.update_status("Shipped")
        self.assertEqual(self.order.get_status(), "Shipped")


if __name__ == '__main__':
    unittest.main()
