a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if(a>b):
    print("Primeiro valor é o: {}".format(a))
    print("Segundo valor é o: {}".format(b))
elif(b>a):
    print("Primeiro valor é o: {}".format(b))
    print("Segundo valor é o: {}".format(a))
else:
    print("Não existe valor maior, os dois são iguais.")