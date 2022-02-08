a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if(a>b):
    print(f"O primeiro valor é maior: {a}")
elif(b>a):
    print(f"Segundo valor é maior: {b}")
else:
    print("Não existe valor maior, os dois são iguais.")