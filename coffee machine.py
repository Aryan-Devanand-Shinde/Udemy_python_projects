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
profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

is_on=True
while is_on:
    choice=input("​What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]    
        print(drink)
        profit=profit + MENU[choice]["cost"]
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        if resources["water"]<=0 or resources["milk"]<=0 and resources["coffee"]<=0:
            print("The machine don't have enough ingredients left")
            is_on=False

