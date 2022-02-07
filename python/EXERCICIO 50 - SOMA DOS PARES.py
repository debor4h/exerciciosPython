soma = 0;
cont = 0
for verific in range(1,7):#um for para contar 6 vezes ele nao conta o 7
    a = int(input("Digite um número: "))
    if a%2==0:#verificando se a divisao da 0
        cont+=1#cont, a cada numero par ele coloca 1 dentro de cont
        soma+=a #esta somando so os que sao pares
print("A soma deu: {} com {} números pares.".format(soma,cont)) #deixar no canto, nao identar pq se nao a cada incremento ele ira mostrar o resultado