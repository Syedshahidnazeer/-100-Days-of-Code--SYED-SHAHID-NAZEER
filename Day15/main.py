MENU = {
    "espresso":{
        "Ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte": {
        "Ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "Ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(ordered_ingredients):
    """Returns true when order can be made, returns false if ingredients are insufficient"""
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water.")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("enter your coins.")
    total = int(input("quarters:")) * 0.25
    total += int(input("dimes:")) * 0.10
    total += int(input("nickles:")) * 0.05
    total += int(input("pennies:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true when the payment is accepted or false if money is insufficient """
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"here is your ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that' not enough money. Money refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    user_input = input(" What would uou like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["Ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_input,drink["Ingredients"])


