Welcome = input("hello welcome to the coffe shop are you ready to order?\n")

Name = input("cool, what is your name?\n")

if Name == "Ben":
    evil_status = input("are you a evil Ben?\n")
    if evil_status == "yes":
        print("you are not welcome here sr please get out of here")
        exit()
    else:
        print("Wecome, so you are one of that good Bens\n")
else:
    print("Wecomen " + Name + " thank you for coming\n")

menu = "black coffee, espresso, latte, cappucino"
 
order = input("please, " + Name + ", tell me what you would like to dink today \nThis is our menu " + menu + ", please let me know your order\n")



if order == "latte":
    price = 15

if order == "black coffee":
    price = 3

if order == "espresso":
    price = 8

if order == "cappucino":
    price = 25

print("cost $" + str(price))

quantity = input("How many " + order + "'s do you want?\n")

print("Great, " + quantity + " " + order + "'s will be served in no time, BRB!\n")

bill = price * int(quantity)

print(bill)
print("the total will be $" + str(bill))