from resources import MENU, resources
from coins import *

resources_machine = {**resources, "money": 0.0}
drinks = ['espresso', 'latte', 'cappuccino']

def view_resources():
    return f'''
        Water:  { resources_machine["water"]  }ml 
        Milk:   { resources_machine["milk"]  }ml
        Coffee: { resources_machine["coffee"] }g
        Money: ${ resources_machine["money"]  }
    '''

def count_coins(quarters: float, dimes: float, nickles: float, pennies: float):
    total = QUARTERS * quarters + DIMES * dimes + NICKLES * nickles + PENNIES * pennies
    return total

def check_resources_machine(order_drink):
    ingredients = MENU[order_drink]['ingredients']

    for ingredient in ingredients:
        drink_ingredient = ingredients[ingredient]
        if drink_ingredient > resources_machine[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True

def make_coffee(order_drink):
    ingredients = MENU[order_drink]['ingredients']

    for ingredient in ingredients:
        drink_ingredient = ingredients[ingredient]
        resources_machine[ingredient] -= drink_ingredient

    return f"Here is your {order_drink} ☕. Enjoy!"

def coffee_machine():
    choose_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose_user == "report":
        print(view_resources())
        return coffee_machine()

    elif choose_user in drinks:
        if(check_resources_machine(choose_user)):
            print("Please insert coins.")
            for coin in coins:
                amount = float(input(f"How many {coin}: "))
                user_coins.update({ coin : amount })

            payment = count_coins( quarters = user_coins['quarters']
                                     , dimes    = user_coins['dimes']
                                     , nickles  = user_coins['nickles']
                                     , pennies  = user_coins['pennies'])

            cost_drink = MENU[choose_user]['cost']

            if payment > cost_drink:
                print(f"Here is ${(payment - cost_drink):.2f} dollars in change.")

            elif payment < cost_drink:
                print("Sorry that's not enough money. Money refunded.")
                return coffee_machine()

            resources_machine["money"] += cost_drink
            print(make_coffee(choose_user))

        return coffee_machine()

    elif choose_user == "off":
        return

    else:
        print("Invalid option. Try again.\n")
        return coffee_machine()

if __name__ == "__main__":
    coffee_machine()
