# Calculadora de IMC
# IMC = peso en (kg) / [estatura(mts)]2
# < 19 : Delgado
# entre 20 y 25: Normal
# entre 26 y 30: Sobrepeso
# > de 30: Obesidad

peso = float(input("Ingrese su peso en KG"))
altura = float(input("cuanto mides en metros?"))
imc = peso / (altura * altura)

print("Su indice de masa corporal es de " + str(imc))

if imc < 20:
    print("estado de delgadez")
if imc >= 20 and imc <=25:
    print("peso normal")
if imc >= 26 and imc <=30:
    print("estado de sobrepeso")
if imc > 30:
    print("estado de obesidad")