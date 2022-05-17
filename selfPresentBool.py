name = input("what is your name?")
age = int(input("how old are you?"))
country = "Nicaragua"
present = "Hello world this is " + name + " im " + str(age) + " im from " + country
calc = 2 * 2

print(present)

if age >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

print(calc)