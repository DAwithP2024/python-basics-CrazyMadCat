# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    try:
        choice = int(input("Select a category by number: ")) - 1
        if 0 <= choice < len(products):
            return choice
    except ValueError:
        pass
    print("Invalid selection. Please try again.")
    return None

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for product, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    return len(name.split()) == 2 and all(part.isalpha() for part in name.split())

def validate_email(email):
    return "@" in email

def main():
    cart = []
    while True:
        name = input("Enter your full name: ")
        if validate_name(name):
            break
        print("Invalid name. Please enter your first and last name.")

    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please include an '@' in the email address.")

    while True:
        category_index = display_categories()
        if category_index is None:
            continue
        category = list(products.keys())[category_index]
        product_list = products[category]
        
        while True:
            display_products(product_list)
            action = input("Choose an option: 1. Buy 2. Sort 3. Back 4. Finish: ")

            if action == "1":
                try:
                    product_choice = int(input("Enter product number to buy: ")) - 1
                    if 0 <= product_choice < len(product_list):
                        quantity = int(input("Enter quantity: "))
                        if quantity > 0:
                            add_to_cart(cart, product_list[product_choice], quantity)
                        else:
                            print("Quantity must be greater than zero.")
                    else:
                        print("Invalid product choice.")
                except ValueError:
                    print("Please enter a valid number.")

            elif action == "2":
                sort_order = input("Sort by price: 1. Ascending 2. Descending: ")
                if sort_order in ["1", "2"]:
                    sorted_products = display_sorted_products(product_list, "asc" if sort_order == "1" else "desc")
                    display_products(sorted_products)

            elif action == "3":
                break

            elif action == "4":
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Enter delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()