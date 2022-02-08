#82 - varios numeros uma lista com tds numeros a outra com os pares e os impares
#criacao das listas
numeros = list()
pares = list()
impares = list()
while True:
  num = int(input('Número: '))
  numeros.append(num)
  if num%2==0:
    pares.append(num)
  else:
    impares.append(num)
  op = ' '
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