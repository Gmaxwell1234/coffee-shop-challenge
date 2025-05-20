 Coffee Shop Challenge
A Python implementation of a coffee shop domain model with Customer, Coffee, and Order relationships.

Features
Customer Management:

Track customer names (1-15 characters)

View order history

See all unique coffees ordered

Coffee Management:

Maintain coffee menu (names ≥3 characters)

Track order statistics

Calculate average price per coffee

Order System:

Record transactions (price validation 
1.0
−
1.0−10.0)

Maintain relationships between customers and coffees

Advanced analytics (top customers per coffee)

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/coffee-shop-challenge.git
cd coffee-shop-challenge
Set up the environment:

bash
pipenv install
pipenv shell
Project Structure
coffee-shop-challenge/
├── models/               # Core domain models
│   ├── __init__.py
│   ├── customer.py       # Customer class
│   ├── coffee.py         # Coffee class
│   └── order.py          # Order class
├── tests/                # Test cases
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── debug.py              # Demo script
├── Pipfile
└── README.md
Usage
Run the demo:

bash
python debug.py
Expected output:

Alice's orders: 2
Alice's coffees: ['Espresso', 'Latte']
Latte's orders: 2
Latte's average price: 4.75
Top customer for Latte: Bob
Run tests:

bash
python -m unittest discover tests
Key Classes
Customer
orders(): Get all orders

coffees(): Get unique coffees ordered

create_order(coffee, price): Make new order

most_aficionado(coffee): Find top spender (class method)

Coffee
orders(): Get all orders

customers(): Get unique customers

num_orders(): Count orders

average_price(): Calculate mean price

Order
Tracks customer, coffee, and price

Validates all inputs

Maintains class list of all orders

Design Patterns
Single Source of Truth: Order class maintains all relationships

Immutability: Coffee names and order prices can't be changed after creation

Type Safety: Strict validation for all properties

Circular Import Resolution: Proper Python module structure

Example Use Case
python
from models.customer import Customer
from models.coffee import Coffee
from models.order import Order

# Create entities
customer = Customer("Sarah")
coffee = Coffee("Cappuccino")

# Place order
order = customer.create_order(coffee, 4.75)

# Get analytics
print(f"{customer.name} has ordered {len(customer.orders())} drinks")
print(f"{coffee.name} has {coffee.num_orders()} orders")