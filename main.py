from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

x=Menu()
x.get_items()
z=CoffeeMaker()
y=MoneyMachine()
i=True
while i:
   a=input('latte 200rs,espresso 100rs,cappuccino 300rs or OFF')
   if a=='latte':
       cost=200
   elif a=="espresso":
       cost=100
   elif a=='cappuccino':
       cost=300
   else:
       i=False
       sys.exit()
   x.find_drink(a)
   
   z.is_resource_sufficient(a)
   z.make_coffee(a)
   z.report()
   
   y.process_coins()
   y.make_payment(cost)
   