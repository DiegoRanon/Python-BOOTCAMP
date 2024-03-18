# JSON 
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

# Variables
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}



# Functions

def show_report():
    print(f"Water : {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

# Loop
while(True):
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        show_report()
    elif choice == "espresso":
        print()
    elif choice == "latte":
        print()
    elif choice == "cappuccino":
        print()
    elif choice == "off":
        break

print("The machine is now off.")

