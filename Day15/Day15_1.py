# pep 8 style guide for python
# two lines after nad before a function
# after comma you should have a space
# built in linter - ability to show the local history
# ability to view the structure of the code
# changing the name function automatically we can refactor everywhere at once
# intelligent enough to differentiate between text and function
# the journey from repl.it to pycharm is like the journey from pencil to pen

# Day15-Project
# create a software for the coffee machine
# 3 hot flavours - operated by coin
# 1-espresso , 2-latte, 3-cappuccino
# resources to be managed
# penny-0.01$,nickel-0.05$,dime0.10$,quarter-0.25$

# program requirements
# 1 print report
# 2 check resources sufficient?
# 3 process coins
# 4 check transaction successful?
# 5 make coffee

user_input = input("What would you like? (espresso/latte/cappuccino)")

def report (Water, Milk, Coffee, Money):
    print(f"Water: {Water}ml")
    print(f"Milk: {Milk}ml")
    print(f"Coffee: {Coffee}g")
    print(f"Money: ${Money}")


if user_input == "espresso" or "latte" or "cappuccino":
    quarters = int(input("quarters:")) * 0.25
    dimes = int(input("dimes:")) * 0.10
    nickles = int(input("nickles:")) * 0.05
    pennies = int(input("pennies:")) * 0.01
    total = quarters + dimes + nickles + pennies
    if user_input == "latte":
        total = total - 1.25
        report(300-50,200,100-18,0)
        print(f"Here is ${total} dollars in change")
        print(f"Here is your latte. Enjoy!")
    elif user_input == "espresso":
        total = total - 2.50
        report(300-200,200-150,100-24,0)
        print(f"Here is ${total} dollars in change")
        print(f"Here is your espresso. Enjoy!")
    elif user_input == "cappuccino":
        total = total - 3.00
        report(300-250,200-100,100-24,0)
        print(f"Here is ${total} dollars in change")
        print(f"Here is your cappuccino. Enjoy!")
    elif total < 0:
        print(f"sir please enter more coins this amount in not sufficient for {user_input}")
else:
    print("Dear customer our machine only has 3 options (espresso/latte/cappuccino)")












