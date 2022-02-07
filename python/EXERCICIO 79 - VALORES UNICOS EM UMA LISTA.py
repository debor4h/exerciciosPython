#79 - usuario digita varios valores numericos, nao pode ter numeros
# iguas, mostrar em ordem crescente (valor adicionado/ valor duplicado)

val = []
while True:
    n = int(input('Digite o número: '))
    if n not in val:
        val.append(n)
        print('Número adicionado.')
    elif n in val:
        print('Número duplicado.')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar [S|N]: ')).upper().strip()
    if op == 'N':
        break;
print('Programa Finalizado!')
val.sort()
print(f'Os números digitados foram: {val}',end='')


#digite varios valores, perguntar se quer continuar
#nao pode digitar numeros repetidos
#se o valor for duplicado exibir uma msg de erro e perguntar se deseja continuar
#Mostrar os valores em ordem 1,2,3
maior = menor =  cont = 0
lista = [] #lista
while True : #enquanto for verdade, faca o bloco
 #l é uma variável criada
  l = (int(input('Digite os valores: '))) #l recebe o que o usuario digita
  if l not in lista: #se l nao estiver na lista
      lista.append(l) #adc na lista o valor l
  else:#senao
      print('Esse número já existe na lista! ')#printar
  op = ' '#iniciando a variavel
  while op !=  'S' and op !=  'N':#enquanto op for diferente de s e n continua com o laco
      op = str(input('Deseja continuar [S|N]?\nOpção:')).upper().strip() #recebendo o que o usuario digita coloca para o maiusculo e tira os espacos
  if op == 'N':#se op for igual a N
      break; #pare a execucao do bloco
print(lista)#mostrar lista
lista.sort()#colocando em ordem crescente
print(lista)#mostrando