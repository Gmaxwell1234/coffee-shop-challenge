from typing import List

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
        
    def orders(self) -> List['Order']:
        """Returns all orders for this customer"""
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self) -> List['Coffee']:
        """Returns unique list of coffees ordered by this customer"""
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        """Creates a new order for this customer"""
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee: 'Coffee') -> 'Customer':
        """Returns customer who spent most on given coffee (or None)"""
        from order import Order
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a Coffee instance")
        
        customers_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer in customers_spending:
                    customers_spending[order.customer] += order.price
                else:
                    customers_spending[order.customer] = order.price
        
        return max(customers_spending.items(), key=lambda item: item[1])[0] if customers_spending else None