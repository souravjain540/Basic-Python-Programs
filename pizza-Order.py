'''
# Pizza Order Program

Entites : 
    1) Pizza  attributes (size, base_price,collection toppings)
    2) Toppings  attributes (name, price)
    3) Order  attributes (pizzas, total_price, discount,status('pending','completed','cancelled') , customer_id)
    4) Customer  attributes (name, phone_number, email, address)  (future extend )
    5) Payment  attributes (order_id, amount, payment_method('cash','card','online'), payment_status('pending','completed','failed'))  (future extend )
    6) Menu  attributes (pizzas, toppings, prices)


MENU = {
    'pizzas': {
        'base_price': 13.00,
        'sizes': {
            'small': {'price_modifier': -2.00, 'diameter': 10},
            'medium': {'price_modifier': 0.00, 'diameter': 12},
            'large': {'price_modifier': 2.00, 'diameter': 14}
        }
    },
    'toppings': {
        'pepperoni': 1.00,
        'mushroom': 0.50,
        'olive': 0.50,
        'anchovy': 2.00,
        'ham': 1.50,
        'extra_cheese': 1.00
    },
    'drinks': {
        'small': 2.00,
        'medium': 3.00,
        'large': 3.50
    },
    'wings': {
        10: 5.00,
        20: 9.00,
        40: 17.50
    }
}

Application Flow:
    1) Welcome and Menu Display
    2) Pizza Selection and customization
    3) Additional Items (Drinks and Wings)
    4) Order Summary and Confirmation
    5) Payment Processing


'''

MENU = {
    'pizza_sizes': {
        'small': {'price_modifier': -2.00, 'diameter': 10},
        'medium': {'price_modifier': 0.00, 'diameter': 12},
        'large': {'price_modifier': 2.00, 'diameter': 14}
    },
    'pizzas': {
        'margherita': {'base_price': 12.00},
        'pepperoni': {'base_price': 14.00},
        'veggie_supreme': {'base_price': 13.50}
    },
    'toppings': {
        'pepperoni': 1.00,
        'mushroom': 0.50,
        'olive': 0.50,
        'anchovy': 2.00,
        'ham': 1.50,
        'extra_cheese': 1.00
    },
    'drinks': {
        'small': 2.00,
        'medium': 3.00,
        'large': 3.50
    },
    'wings': {
        10: 5.00,
        20: 9.00,
        40: 17.50
    }
}

class Pizza:
    
    def __init__(self,name='margherita',size='medium'):
        self.name = name
        self.size = size
        self.toppings = []
        self.order_items = []
        self.total_cost = 0.0
    
    @staticmethod
    def display_menu():
        print("\n🍕 Welcome to Python Pizza 🍕\n")

        print("--------- PIZZAS ---------")
        for pizza_name, pizza_data in MENU['pizzas'].items():
            print(f"\n{pizza_name.replace('_',' ').title()}:")
            base = pizza_data['base_price']
            for size, info in MENU['pizza_sizes'].items():
                price = base + info['price_modifier']
                print(f"  {size.title():<10} ({info['diameter']}”): ${price:.2f}")

        print("\n---- TOPPINGS ----")
        for topping, price in MENU['toppings'].items():
            print(f"{topping.replace('_', ' ').title():<15} ${price:.2f}")

        print("\n---- DRINKS ----")
        for size, price in MENU['drinks'].items():
            print(f"{size.title():<10} ${price:.2f}")

        print("\n---- WINGS ----")
        for qty, price in MENU['wings'].items():
            print(f"{str(qty)+' pcs':<10} ${price:.2f}")

        print("\n--------------------------")
        print("⭐ Choose your pizza, size, and toppings")
        print("⭐ Add drinks & wings for a combo deal\n")


    def choose_pizza(self):
        while True:
            choice = input("Choose a pizza (margherita, pepperoni, veggie_supreme): ").strip().lower()
            if choice in MENU['pizzas']:
                self.name = choice
                base_price= MENU['pizzas'][choice]['base_price']
                self.total_cost += base_price
                self.order_items.append((choice, base_price))
                break
            else:
                print("Invalid choice. Please try again.")

    def choose_size(self):
        while True:
            size = input("Choose a size (small, medium, large): ").strip().lower()
            if size in MENU['pizza_sizes']:
                self.size = size
                size_modifier = MENU['pizza_sizes'][size]['price_modifier']
                self.total_cost += size_modifier
                self.order_items.append((size, size_modifier))
                break
            else:
                print("Invalid size. Please try again.")

    def choose_toppings(self):
        while True:
            topping = input("Add a topping (type 'done' when finished): ").strip().lower()
            if topping == 'done':
                break
            elif topping in MENU['toppings']:
               price = MENU['toppings'][topping]
               self.total_cost += price
               self.toppings.append(topping)
               self.order_items.append((topping, price))

            else:
                print("Invalid topping. Please try again.")

    def calculateBill(self):
        print("\n --- ORDER SUMMARY ---")
        for item ,price in self.order_items:
            print(f"{item.replace('_',' ').title():<20} ${price:.2f}")
        print("-"*35)
        print(f"\nTotal Cost: ${self.total_cost:.2f}")

    def order(self):
        print("WELCOME TO PYTHON PIZZA!")
        print("Here's our menu:")
        self.display_menu()

        self.choose_pizza()
        self.choose_size()
        self.choose_toppings()

        self.calculateBill()
    
p1 = Pizza()
p1.order()
