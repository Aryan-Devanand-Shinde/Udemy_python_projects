from coffee_maker import CoffeeMaker
from menu import Menu,MenuItem
from money_machine import MoneyMachine

items_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

def report():
    coffee_machine.report()
    money_machine.report()

machine_on=True
while(machine_on):
    customer_choice  = input(f"​What would you like? {items_menu.get_items()} \n 'report' to get the report \n 'off' ot turn off the machine\n ").lower()
    print(" ")
    print(f"your choice is '{customer_choice}'\n")
    if customer_choice=='report':
        report()
    elif customer_choice=='off':
        machine_on=False
        report()
        break    
    else:
        drink = items_menu.find_drink(customer_choice) 
        print(drink)

        if coffee_machine.is_resource_sufficient(drink)==True:
            print(money_machine.make_payment(drink.cost))
            coffee_machine.make_coffee(drink)   
     
            



