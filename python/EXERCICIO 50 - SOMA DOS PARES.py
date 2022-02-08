soma = cont =  0
for verifica in range(1,7):
    a = int(input("Digite um número: "))
    if a%2==0:
        cont+=1
        soma+=a
print("A soma deu: {} com {} números pares.".format(soma,cont))