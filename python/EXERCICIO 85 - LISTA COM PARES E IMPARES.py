#criando listas
numeros = []
pares = list()
impares = list()

for n in range(1,8):
    num = int(input(f'Digite o {n} valor: '))
    numeros.append(num)
    if num%2==0:
        pares.append(num)
    elif num%2==1:
        impares.append(num)
print('-'*70)
#colocando em ordem numericas
pares.sort()
impares.sort()
#imprimindo
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')
