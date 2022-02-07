# numeros = [[],[]] lista maior e o numero [par],[impar]

numeros = [[],[]] #aqui é uma lista com duas dentro, duas listas internas
while True:
    n=int(input('Número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 != 0:
        numeros[1].append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar[S|N]: ')).upper().strip()
    if op == 'N':
        break;
print(f'Todos os números ímpares são: {numeros[1]}')
print(f'Todos os números pares são: {numeros[0]}')
print(f'Todos os números são: {numeros}')


# numeros = [[],[]] lista maior e o numero [par],[impar]
#if valor %2==0:
#0 e o primeiro indice, 1 e o segundo indice
#numeros[0].append(valor)
#criando listas
numeros = []
pares = list()
impares = list()
#para n no intervalo de 1 a 7
for n in range(1,8):
    num = int(input(f'Digite o {n} valor: '))#digite o numero
    numeros.append(num)#adicionar num dentro da lista numeros
    if num%2==0:
        pares.append(num)#se ele for par colocar dentro dessa lista
    elif num%2==1:
        impares.append(num)#se nao colocar na lista do impar
print('-'*70)
#colocando em ordem numericas
pares.sort()
impares.sort()
#imprimindo
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')

print('=-'*70)
#lista unico com duas dentro
num1=[[],[]]#aqui tem uma lista aonde tem duas listas dentro uma pra par e a outra pra impar
for sete in range(1,8):
    n1=int(input(('Digite um número: ')))
    num1.append(n1) #aqui esta adicionando na lista
    if n1%2==0:
        num1[0].append(n1)
    elif n1%2!=0:
        num1[1].append(n1)
print(f'Todos os números são {num1}')
num1[0].sort()#aqui esta em ordem
print(f'Todos os números pares {num1[0]}')
num1[1].sort()#aqui esta em ordem
print(f'Todos os números ímpares {num1[1]}')
