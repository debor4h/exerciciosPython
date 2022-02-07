#82 -varios numeros uma lista com tds numeros
#a outra com os pares e os impares
par = list()
impar = []
numeros = []

while True:
    n=int(input('Digite os números: '))
    numeros.append(n)
    if n%2==0:
        par.append(n)
    elif n%2!=0:
        impar.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S|N]: ')).upper().strip()
    if op == 'N':
        break;
print('=-'*20)
print(f'Todos os números: {numeros}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
print('=-'*20)

#ler varios numeros s/n
#ter 2 listas extras
#uma lista so com os numeros pares
#uma list so com os impares
#uma lista com todos valores
#mostrar tds
#mundo 2 tem looping
numeros = [] #lista de tds os numeros
impares = []#lista dos impares
pares = []#lista dos pares
#lista e vetor
#ou pares = list()
while True: #enquanto verdaded
    n = (int(input('Digite os números: ')))#recebe o q o usuario digitar
    numeros.append(n)#numeros(lista).inserir o n (digitado pelo teclado)
    if n%2==0:#if n modulo de 2 for igual a 0
        pares.append(n) #adicionar o numero na lista pares
    elif n%2!=0: #se nao
        impares.append(n)#adicionar o numero na lista impares
    op = ' '#declarando vazio
    while op != 'S' and op != 'N':#enquanto op for diferente de S e N, repita a pergunta
        op = str(input('Deseja continuar [S|N]: ')).upper().strip()#passado para o maiusculo e tira os espacos iniciais e finais
    if op == 'N':#se op for n
        break;#pare
print(f'Números {numeros}')#mostrar tds os numeros
print(f'Pares {pares}')#mostrar os numeros pares
print(f'Ímpares {impares}')#mostrar os numeros impares


#82 - varios numeros uma lista com tds numeros a outra com os pares e os impares
#criacao das listas
numeros = list()
pares = list()
impares = list()
while True:
  num = int(input('Número: '))
  numeros.append(num)
  if num%2==0:#se sim adiciona em par
    pares.append(num)
  else:#se nao adiciona em impar
    impares.append(num)
  op = ' '#validando
  while op != 'S' and op != 'N':
    op = str(input('Deseja continuar [S|N]: ')).upper()
  if op == 'N':
    break;
print()
print('*'*30)
print()
print(f'Todos os números: {numeros}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')