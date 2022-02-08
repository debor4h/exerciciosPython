from datetime import date #necessario para data

anoNascimento = int(input("Qual ano de nascimento: "))
ano = date.today().year
idade = ano - anoNascimento

if(idade<=9):
    print ("Idade: ",idade)
    print("Classificação: Mirim")
elif(idade<=14):
    print("Idade: ",idade)
    print("Classificação: Infantil")
elif(idade<=19):
    print("Idade: ",idade)
    print("Classificação: Junior")
elif(idade<=20):
    print("Idade: ",idade)
    print("Classificação: Sênior")
else:
    print("Idade: ",idade)
    print("Classificação: Master")