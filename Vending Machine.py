def display_menu(products):
    print("\nWelcome to the Vending Machine")
    for category, items in products.items():
        print(f"{category}:\n")
        print("Code\tProduct\t\tPrice\tQuantity")
        for code, product in items.items():
            tab_spacing ="\t" if len(product['name']) < 8 else ""
            print(f"{code}\t{product['name']}{tab_spacing}\t${product['price']:.2f}\t{product['quantity']}")

def select_product(products, balance):
    while True:
        code = input("\nEnter the product code: ").upper()
        category, product = None, None
        for cat, items in products.items():
            if code in items:
                category = cat
                product = items[code]
                break
        if product:
            while product['quantity'] > 0 and balance < product['price']:
                print("\nInsufficient balance. Please insert more money.")
                balance = insert_money(balance)
            if product['quantity'] > 0:
                balance -= product['price']
                product['quantity'] -= 1
                print(f"\nDispensing {product['name']}...")
                print(f"Remaining Balance: ${balance:.2f}")
                print(f"Remaining {product['name']} quantity: {product['quantity']}")
                return category, code
            elif product['quantity'] == 0:
                print("\nSorry, this product is out of stock.")
            else:
                print("\nInsufficient balance. Please insert more money.")
        else:
            print("\nInvalid choice. Please enter a valid product code.")

def insert_money(balance):
    while True:
        money_input = input("\nInsert money (in dollars): ")
        if money_input.replace('.', '', 1).isdigit():
            money = float(money_input)
            if money > 0:
                balance += money
                print(f"Current Balance: ${balance:.2f}")
                break
            elif money < 0:
                print("Invalid amount. Please insert a positive amount.")
            else:
                print("Enter the currency in digit form.")
        else:
            print("Invalid input. Please enter a numeric amount.")
    return balance

def vending_machine(products):
    display_menu(products)
    balance = 0
    total_spent = 0
    while True:
        if balance <= 0:
            balance = insert_money(balance)
        selected_category, selected_code = select_product(products, balance)
        if selected_category and selected_code:
            total_spent += products[selected_category][selected_code]['price']
            balance -= products[selected_category][selected_code]['price']
            more_purchase = input("\nDo you want to make another purchase? (yes/no): ").lower()
            if more_purchase == 'no':
                change = balance if balance >= 0 else 0
                print(f"Total spent: ${total_spent:.2f}")
                print(f"Change: ${change:.2f}")
                print("Thank you for using Vending Machine. Have a nice day!")
                break

# Assortment of items available in the Vending Machine
products = {
    'Snacks': {
        'E1': {'name':'Ice cream','price': 4.00, 'quantity':8},
        'E2': {'name':'Chips','price': 2.00, 'quantity':10},
        'E3': {'name':'Chocolates','price': 3.50, 'quantity':15}
    },
    'Drinks': {
        'F1': {'name':'Juice','price': 2.00,'quantity':15},
        'F2': {'name':'Red Bull','price':8.00,'quantity':5},
        'F3': {'name':'Water','price': 1.00,'quantity':20}
    },
    'Coffee':{
        'G1': {'name':'espresso','price':15.00,'quantity':8},
        'G2': {'name':'Cappuccino','price':5.00,'quantity':5},
        'G3': {'name':'Cafe Latte','price':24.00,'quantity':10}
        }
}

vending_machine(products)