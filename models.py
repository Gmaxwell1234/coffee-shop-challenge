class Customer:
    def __init__(self, name):
        self.name = name  # Using the property setter
        
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
        
    def orders(self):
        """Returns all orders for this customer"""
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        """Returns unique list of coffees ordered by this customer"""
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        """Creates a new order for this customer"""
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        """Returns customer who spent most on given coffee (or None)"""
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a Coffee instance")
        
        customers_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer in customers_spending:
                    customers_spending[order.customer] += order.price
                else:
                    customers_spending[order.customer] = order.price
        
        if not customers_spending:
            return None
            
        return max(customers_spending.items(), key=lambda item: item[1])[0]


class Coffee:
    def __init__(self, name):
        self.name = name  # Using the property setter
        
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
        
    def orders(self):
        """Returns all orders for this coffee"""
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        """Returns unique list of customers who ordered this coffee"""
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        """Returns total number of orders for this coffee"""
        return len(self.orders())
    
    def average_price(self):
        """Returns average price of orders for this coffee"""
        if not self.orders():
            return 0
        return sum(order.price for order in self.orders()) / len(self.orders())


class Order:
    all = []  # Class variable to store all orders
    
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price  # Using the property setter
        Order.all.append(self)
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after initialization")
        self._price = value
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value