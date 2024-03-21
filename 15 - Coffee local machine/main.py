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
    "water": 100,
    "milk": 200,
    "coffee": 100
}
QUARTERS_PRICE = 0.25
DIMES_PRICE = 0.10
NICKLES_PRICE = 0.05
PENNIES_PRICE = 0.01



# Functions

def show_report():
    print(f"Water : {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
def produceCoffee(type):
    if check_Resources(type):
        use_Resources(type)
    else:
        if(MENU[type]["ingredients"]["water"] > resources['water']):
            print("Sorry there is not enought water.")
        elif(MENU[type]["ingredients"]["coffee"] > resources['coffee']):
            print("Sorry there is not enought coffee.")
        
        if(type != "espresso"):
            if(MENU[type]["ingredients"]['milk'] > resources['milk']):
                print("Sorry there is not enought milk.")

def use_Resources(type):
    resources['water'] = resources['water'] - MENU[type]["ingredients"]["water"]
    resources['coffee'] = resources['coffee'] - MENU[type]["ingredients"]["coffee"]
    if type != "espresso":
        resources['milk'] = resources['milk'] - MENU[type]["ingredients"]["milk"]
    print(f"{resources['water']}\n{resources['coffee']}\n{resources['milk']}")

def check_Resources(type):
    if type == "espresso":
        return (MENU[type]["ingredients"]["water"] <= resources['water'] and MENU[type]["ingredients"]["coffee"] <= resources['coffee'])
    else:
        return (MENU[type]["ingredients"]["water"] <= resources['water'] and MENU[type]["ingredients"]["coffee"] <= resources['coffee'] and MENU[type]["ingredients"]['milk'] <= resources['milk'])

def check_processCoins(price):
    print("Please insert coins.")
    quarters = input("How many quarters?:")
    dimes = input("How many dimes?:")
    nickles = input("How many nickles?:")
    pennies = input("How many pennies?:")
    total = (QUARTERS_PRICE * quarters) + (DIMES_PRICE * dimes) + (NICKLES_PRICE * nickles) + (PENNIES_PRICE * pennies)
    return total


# Loop
while(True):
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        show_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        produceCoffee(choice)
    elif choice == "off":
        break

print("The machine is now off.")

