MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def ingredient_sufficiency(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {[item]}")
            return False
    return True

def coin_processing():
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def is_money_transacted(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry there is not enough money, Please insert enough coins")
        return False

def make_coffee(drink_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!.")

is_on = True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if ingredient_sufficiency(drink["ingredients"]):
            payment = coin_processing()
            if is_money_transacted(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
