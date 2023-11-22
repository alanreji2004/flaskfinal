from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def generate_invoice(customer_name, items):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_amount = sum(item['quantity'] * item['price'] for item in items)

    rendered_template = template.render(
        date=date,
        customer_name=customer_name,
        items=items,
        total_amount=total_amount
    )

    with open('invoice.html', 'w') as file:
        file.write(rendered_template)

if __name__ == '__main__':
    customer_name = "John Doe"
    items = [
        {"name": "Item 1", "quantity": 2, "price": 20.0},
        {"name": "Item 2", "quantity": 1, "price": 30.0},
        {"name": "Item 3", "quantity": 3, "price": 10.0}
    ]

    generate_invoice(customer_name, items)

    print("Invoice generated. Check 'invoice.html'.")
    