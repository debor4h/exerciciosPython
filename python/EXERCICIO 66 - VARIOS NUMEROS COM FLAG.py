num = soma = cont = 0
while True:
    num = int(input('Digite os números (999 para parar): '))
    if num == 999: #aqui é o flag
        break;
    cont += 1#colocar aqui se colocar encima ele vai contar o 999
    soma = soma + num
print(f'Quantidade de números digitados: {cont}')
print(f'Soma dos números digitados: {soma}')