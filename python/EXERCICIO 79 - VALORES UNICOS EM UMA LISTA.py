#digite varios valores, perguntar se quer continuar
#nao pode digitar numeros repetidos
#se o valor for duplicado exibir uma msg de erro e perguntar se deseja continuar
#Mostrar os valores em ordem 1,2,3

maior = menor =  cont = 0
lista = [] #lista
while True : #enquanto for verdade, faca o bloco
  l = (int(input('Digite os valores: ')))
  if l not in lista:
      lista.append(l)
  else:
      print('Esse número já existe na lista! ')
  op = ' '
  while op !=  'S' and op !=  'N':
      op = str(input('Deseja continuar [S|N]?\nOpção:')).upper().strip()
  if op == 'N':
      break;
print(lista)
lista.sort()
print(lista)