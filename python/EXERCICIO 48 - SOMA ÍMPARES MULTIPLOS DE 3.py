#somar impares multiplos de 3
soma = 0
cont = 0;
#laco impares no intervalo de 1 ate 500 pulando de 2 em 2
for impares in range(1,501,2): #pq como comeca do 1 ele vai terminar sendo impar
    if impares%3 == 0: #aqui ele verifica os que sao divisiveis
        cont = cont+1; #contador
        print(impares, end=' ')  # esse end ele vai permiter o numero um do lado do outro
        soma+=impares #acumulador

print("\nSOMA deu {} com {} números ímpares.".format(soma,cont))
