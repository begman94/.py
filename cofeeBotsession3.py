#Let's play with some numbers

Welcome = input("hello welcome to the coffe shop are you ready to order?\n")

Name = input("cool, what is your name?\n")

menu = "black coffee, espresso, latte, cappucino"

order = input("cool, " + Name + ", this is our menu, " + menu + ", please let me know your order \n:D \n")

quantity = input("great, how many " + order + "'s do you want?\n")

price = 10

print("Great, " + quantity + " " + order + "'s will be served in no time, BRB! ;D")

bill = price * int(quantity)

print(bill)
print("the total will be $" + str(bill))