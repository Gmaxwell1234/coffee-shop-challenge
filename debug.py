from models import Customer, Coffee, Order

def main():
    # Create customers
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    
    # Create coffees
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    
    # Create orders
    order1 = Order(customer1, coffee1, 4.5)
    order2 = Order(customer1, coffee2, 3.0)
    order3 = Order(customer2, coffee1, 5.0)
    
    # Test relationships
    print(f"{customer1.name}'s orders: {len(customer1.orders())}")  # Should be 2
    print(f"{customer1.name}'s coffees: {[c.name for c in customer1.coffees()]}")  # Should be ['Latte', 'Espresso']
    
    print(f"{coffee1.name}'s orders: {coffee1.num_orders()}")  # Should be 2
    print(f"{coffee1.name}'s average price: {coffee1.average_price():.2f}")  # Should be 4.75
    
    # Test bonus method
    top_customer = Customer.most_aficionado(coffee1)
    print(f"Top customer for {coffee1.name}: {top_customer.name if top_customer else 'None'}")  # Should be Alice

if __name__ == "__main__":
    main()