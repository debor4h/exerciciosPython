from datetime import date #necessario para data

idade = int(input("Qual ano de nascimento: "))
ano = date.today().year
i = ano - idade;

if(i<=9):
    print ("Idade: ",i)
    print("Classificação: Mirim")
elif(i<=14):
    print("Idade: ",i)
    print("Classificação: Infantil")
elif(i<=19):
    print("Idade: ",i)
    print("Classificação: Junior")
elif(i<=20):
    print("Idade: ",i)
    print("Classificação: Sênior")
else:
    print("Idade: ",i)
    print("Classificação: Master")