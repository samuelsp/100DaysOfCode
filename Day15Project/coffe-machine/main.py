from resources import MENU, resources
from coins import *

resources_machine = {**resources, "money": 0.0}
drinks = ['espresso', 'latte', 'cappuccino']

def view_resources(resources_machine):
    return f'''
        Water:  { resources_machine["water"]  }ml 
        Milk:   { resources_machine["milk"]  }ml
        Coffee: { resources_machine["coffee"] }g
        Money: ${ resources_machine["money"]  }
    '''

def count_coins(quarters: float, dimes: float, nickles: float, pennies: float):
    total = QUARTERS * quarters + DIMES * dimes + NICKLES * nickles + PENNIES * pennies
    return total

def check_resources_machine(resources_machine, drink_selected):
    ingredients = MENU[drink_selected]['ingredients']

    if 'water' in ingredients:
        water = ingredients["water"]
        if water > resources_machine["water"]:
            print("Sorry there is not enough water.")
            return False

    if 'milk' in ingredients:
        milk = ingredients["milk"]
        if milk > resources_machine["milk"]:
           print("Sorry there is not enough milk.")
           return False

    if 'coffe' in ingredients:
        coffee = ingredients["coffee"]
        if coffee > resources_machine["coffee"]:
           print("Sorry there is not enough coffee.")
           return False

    return True

def make_coffee(resources_machine, chosen_drink):
    ingredients = MENU[chosen_drink]['ingredients']

    if 'water' in ingredients:
        water = ingredients["water"]
        resources_machine["water"] -= water

    if 'milk' in ingredients:
        milk = ingredients["milk"]
        resources_machine["milk"] -= milk

    if 'coffee' in ingredients:
        coffee = ingredients["coffee"]
        resources_machine["coffee"] -= coffee

    return f"Here is your {chosen_drink}. Enjoy!"

def coffee_machine():
    choose_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose_user == "report":
        print(view_resources(resources_machine))
        return coffee_machine()

    elif choose_user in drinks:
        if(check_resources_machine(resources_machine, choose_user)):
            print("Please insert coins.")
            for coin in coins:
                amount = float(input(f"How many {coin}: "))
                user_coins.update({ coin : amount })

            total_coins = count_coins( quarters = user_coins['quarters']
                                     , dimes    = user_coins['dimes']
                                     , nickles  = user_coins['nickles']
                                     , pennies  = user_coins['pennies'])

            cost_drink = MENU[choose_user]['cost']

            if total_coins > cost_drink:
                print(f"Here is ${(total_coins - cost_drink):.2f} dollars in change.")

            elif total_coins < cost_drink:
                print("Sorry that's not enough money. Money refunded.")
                return coffee_machine()

            print(make_coffee(resources_machine, choose_user))
            resources_machine["money"] += cost_drink

        return coffee_machine()

    elif choose_user == "off":
        return

    else:
        print("Invalid option. Try again.\n")
        return coffee_machine()

if __name__ == "__main__":
    coffee_machine()
