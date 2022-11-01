import sys
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    ingredients={"latte":{'water':200,'milk':150,'coffee':24},"espresso":{'water':50,'milk':0,'coffee':18},"cappuccino":{'water':250,'milk':50,'coffee':24}}
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in self.ingredients[drink]:
            if self.ingredients[drink][item]> self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
                sys.exit()
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in self.ingredients[order]:
            self.resources[item] -= self.ingredients[order][item]
        print(f"Here is your {order} ☕️. Enjoy!")



  