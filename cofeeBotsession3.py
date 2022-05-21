#Let's play with some numbers

from unicodedata import name


Welcome = input("hello welcome to the coffe shop are you ready to order?\n\n")

Name = input("cool, what is your name?\n\n")

if name == "Ben":
    print("you are not welcome here sr please get out of here")
else:
    print("Wecomen " + Name + " thank you for coming\n")

menu = "black coffee, espresso, latte, cappucino"
 
order = input("please, " + Name + ", tell me what you would like to dink today \n\nThis is our menu " + menu + ", please let me know your order \n\n:D \n\n")

quantity = input("great, how many " + order + "'s do you want?\n\n")

price = 10

print("Great, " + quantity + " " + order + "'s will be served in no time, BRB! \n\n;D\n\n")

bill = price * int(quantity)

print(bill)
print("the total will be $" + str(bill))

if 2 > 3:
    print("yep is true")
else:
    print("no is not true")