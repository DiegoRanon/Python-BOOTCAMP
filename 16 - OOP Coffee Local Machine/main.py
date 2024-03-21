from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize Objects
menu = Menu()
items = menu.menu
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()

def getItem(choice):
    for item in items:
        if(item.name == choice):
            return item

# Program
while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if menu.find_drink(choice):
            item = getItem(choice)
            if coffeeMachine.is_resource_sufficient(item):
                if moneyMachine.make_payment(item.cost):
                    coffeeMachine.make_coffee(item)

    elif choice == "report":
        coffeeMachine.report()
        moneyMachine.report()
    elif choice == "off":
        break
    else:
        print("This option doesn't exist")

print("Coffee machine is now off.")