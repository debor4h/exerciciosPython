num = soma = cont = 0
while True:
    num = int(input('Digite os números (888 ara parar): '))
    if num == 888: #aqui é o flag
        break;
    cont += 1#colocar aqui se colocar encima ele vai contar o 888
    soma = soma + num
print(f'Quantidade de números digitados: {cont}')
print(f'Soma dos números digitados: {soma}')