#somar impares multiplos de 3
soma = 0
cont = 0;
#laco impares no intervalo de 1 ate 500 pulando de 2 em 2
for impares in range(1,501,2):
    if impares%2 != 0:
        cont = cont+1
        print(impares, end=' ')
        soma+=impares
print()
print(f"SOMA deu {soma} com {cont} números ímpares.")
