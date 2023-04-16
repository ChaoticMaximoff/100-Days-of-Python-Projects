from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ").lower()

    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(user_input)

        if not coffee_maker.is_resource_sufficient(order):
            print("Sorry there is not enough water.")
        else:
            if not money_machine.make_payment(order.cost):
                print("Sorry that's not enough money. Money refunded.")
            else:
                coffee_maker.make_coffee(order)


