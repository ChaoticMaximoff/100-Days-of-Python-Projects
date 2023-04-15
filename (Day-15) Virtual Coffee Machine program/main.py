from data import MENU, resources


# TODO: 3. print report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# TODO: 4. check resources
def check_resources(order):
    n_water = MENU[order]['ingredients']['water']
    n_milk = MENU[order]['ingredients']['milk']
    n_coffee = MENU[order]['ingredients']['coffee']
    if n_water <= resources['water']:
        if n_milk <= resources['milk']:
            if n_coffee <= resources['coffee']:
                return True
            else:
                return "coffee"
        else:
            return "milk"
    else:
        return "water"


# TODO: 5. process coins
def process_payment(order):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    if total >= MENU[order]["cost"]:
        resources["money"] += MENU[order]["cost"]
        change = total - MENU[order]["cost"]
        print(f"Here's ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# TODO: 7. make coffee
def make_coffee(order):
    available = check_resources(order)

    if available == True:
        # TODO: 6. check if the transaction was successful
        if process_payment(order):
            resources['milk'] -= MENU[order]['ingredients']['milk']
            resources['water'] -= MENU[order]['ingredients']['water']
            resources['coffee'] -= MENU[order]['ingredients']['coffee']
            print(f"Here is your {order} ☕. Enjoy!")
    else:
        print(f"Sorry, there's not enough {available}.")


machine_on = True
commands = ["off", "report", "espresso", "cappuccino", "latte"]

while machine_on:
    # TODO: 1. prompt user
    user_input = input("    What would you like? (espresso/latte/cappuccino): ").lower()

    while user_input not in commands:
        user_input = input("    You entered a wrong command, check your spelling.\n    What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print_report()

    elif user_input == "off":
        # TODO: 2. turn off machine by entering "off" prompt
        machine_on = False

    else:
        make_coffee(user_input)
