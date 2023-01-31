MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 35
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 18,
        },
        "cost": 50,
    },

    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 75,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    "Return True when the payment id accepted, or False if money is insufficient."
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many of 10?: ")) * 10
    total += int(input("how many of 20?: ")) * 20
    total += int(input("how many of 50?: ")) * 50
    total += int(input("how many of 100?: ")) * 100
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

def refill():
    """Refill the coffee machine for new coffee"""
    global resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }


profit = 0
is_on = True
while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").strip()
    # print(choice,len(choice))
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}l")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    elif choice == "refill":
        refill()
        print(f"Water: {resources['water']}l")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


