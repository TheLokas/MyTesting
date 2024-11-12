class Product:
    def __init__(self, name: str, price: float, stock_quantity: int):
        self.name = name                   # Название товара
        self.price = price                 # Цена товара
        self._stock_quantity = stock_quantity  # Количество товара на складе (защищённое поле)

    def get_name(self):
        # Получение названия товара
        return self.name

    def get_price(self):
        # Получение цены товара
        return self.price

    def get_stock_quantity(self):
        # Получение количества товара на складе
        return self._stock_quantity

    def _update_stock(self, quantity: int):
        """Защищённый метод для обновления количества товара на складе."""
        if self._stock_quantity >= quantity:
            self._stock_quantity -= quantity
            return True
        return False  # Если товара недостаточно на складе, возвращаем False




class Order:
    def __init__(self):
        self.products = []           # Список добавленных в заказ товаров
        self.total_cost = 0.0         # Общая стоимость заказа
        self._status = "Pending"      # Статус заказа (защищённое поле)

    def add_product(self, product: Product, quantity: int):
        """Добавление товара в заказ, если на складе есть нужное количество."""
        if product._update_stock(quantity):  # Проверка наличия товара на складе
            self.products.append((product, quantity))  # Добавляем товар в список заказа
            self._calculate_total_cost(product, quantity)  # Обновляем общую стоимость заказа
        else:
            print(f"Недостаточно товара на складе: {product.get_name()}")

    def _calculate_total_cost(self, product: Product, quantity: int):
        """Защищённый метод для расчета общей стоимости заказа."""
        self.total_cost += product.get_price() * quantity  # Добавляем стоимость товара к общей сумме

    def update_status(self, new_status: str):
        """Обновление статуса заказа."""
        self._status = new_status

    def get_total_cost(self):
        # Получение общей стоимости заказа
        return self.total_cost

    def get_status(self):
        # Получение текущего статуса заказа
        return self._status
