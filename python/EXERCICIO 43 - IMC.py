altura = float(input("Informe a sua altura (M): "))
peso = float(input("Informe o seu peso (KG): "))
imc = peso / (altura*altura)
print("IMC: {:.2f}".format(imc))
if(imc <18.5):
    print("Abaixo do peso")
elif (imc <=25):
    print("Peso ideal")
elif(imc <=30):
    print("Sobrepeso")
elif(imc <=35):
    print("Obesidade Grau 1")
elif(imc <=40):
    print("Obesidade Grau 2")
else:
    print("Obesidade Mórbida")