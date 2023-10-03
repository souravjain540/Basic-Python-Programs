import time
contents = {
    "milk": 1500,
    "water": 2000,
    "coffee": 500,
}

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 100
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 200
    }
}
while True:
    order = input("What would you like to have? (latte/espresso/cappuccino): ").lower()
    try:
        for key, val in menu[order]["ingredients"].items():
            if val < contents[key]:
                available = 1
            else:
                print(f"Sorry there are not enough {key}")
                available = 0
                break
        if available == 1:
            five = int(input("No.of 5 rupee coins: "))
            ten = int(input("No.of 10 rupee coins:"))
            twenty = int(input("No.of 20 rupee coins: "))
            amount = five * 5 + ten * 10 + twenty * 20
            if amount > menu[order]["cost"]:
                change = amount - menu[order]["cost"]
                print(f"Here is your change of {change} rupees")
                paid = 1
            elif amount < menu[order]["cost"]:
                print(f"Sorry, the cost of {order} is {menu[order]['cost']}")
                print(f"returning your {amount} rupees.")
                paid = 0
            else:
                paid = 1
        if paid == 1 and available == 1:
            for key, val in menu[order]["ingredients"].items():
                contents[key] -= val
            print(f"Here is your {order}.")

    except KeyError:
        if order == "report":
            for key, value in contents.items():
                print(f"{key}: {value}")
        elif order == "refill":
            print("Refilling...")
            filler = {
                "milk": 1500,
                "water": 2000,
                "coffee": 500
            }
            if contents != filler:
                contents = filler
                time.sleep(2)
            else:
                print("The machine is already full.")
        elif order == "off":
            break
