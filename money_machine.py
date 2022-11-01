class MoneyMachine:

    CURRENCY = "₹"

    VALUES = {
        "100": 100,
        "200": 200,
        "500": 500,
        "2000":2000,
        "50":50,
        "10":10,
        "5":5,
        "2":2,
        "1":1,
    }

    def __init__(self):
        self.money_received = 0

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert money")
        for note in self.VALUES:
            self.money_received += int(input(f"How many {note}?: "))*self.VALUES[note]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False


