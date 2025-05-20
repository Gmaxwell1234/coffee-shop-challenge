from typing import List

class Coffee:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value
        
    def orders(self) -> List['Order']:
        """Returns all orders for this coffee"""
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self) -> List['Customer']:
        """Returns unique list of customers who ordered this coffee"""
        return list({order.customer for order in self.orders()})
    
    def num_orders(self) -> int:
        """Returns total number of orders for this coffee"""
        return len(self.orders())
    
    def average_price(self) -> float:
        """Returns average price of orders for this coffee"""
        orders = self.orders()
        return 0 if not orders else sum(order.price for order in orders) / len(orders)