#81 - usuario digita [sn] quantos numeros
#foram digitados, lista em forma descrente e se o 5 esta na lista
n=[]
while True:
    n.append(int(input('Digite o número: ')))
    op = ' '
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar[S|N]: ')).upper().strip()
    if op == 'N':
        break;
print('-='*50)
if 5 in n:
    print('O número 5 está na lista.')
elif 5 not in n:
    print('O número 5 não está na lista.')
print(f'Foram digitados {len(n)} números.')
print(f'Os valores digitados foram: ',end='')
print(*n,sep=',')
n.sort(reverse=True)
print(f'Os valores em ordem decrescente são {n}')


#ler varios numeros, de acordo com o usuario s|n
#quantos numeros foram digitados
#lista de valores ordenada em forma decrescente maior p menor
#se o valor 5 foi digitado na lista
valor = [] #lista vazia
while True:#enquanto for verdadeiro
    valor.append(int(input('Digite os números: ')))#append inseri, pelo teclado o q o usuario digitar
    op = ' ' #comeca uma string vazia
    while op != 'S' and op !='N': #enquanto op for diferente de s ou n faca a pergunta
        op=str(input('Deseja continuar [S/N]?\nOpção: ')).upper().strip()#maiusculo e tira os espacos iniciais e finais
    if op =='N':#se op for igual a n
        break;#pare
if 5 in valor:#se 5 estiver na lista valor
    print('O número 5 foi digitado.')#printar
else:
    print('O número 5 não foi digitado.')   #se nao
print(f'Foram digitados {len(valor)} números.')#len ele conta a quantidade de uma lista
valor.sort(reverse=True)#ordem decrescente, True em maiusculo, primeiro faz isso
print(f'Valores em ordem decrescente {valor}')#depois mostra





#81 - usuario digita [sn] quantos numeros foram digitados, lista em forma descrente e se o 5 esta na lista

dados = list() #criando a lista
while True: #looping infinito
  numero = int(input('Informe o número: ')) #perguntando valor
  dados.append(numero) #adicionando numero na lista
  resposta = ' ' #validando
  while resposta != 'S' and resposta!='N':
    resposta = str(input('Deseja continuar [S|N]: ')).upper()
  if resposta == 'N': #se for break, para
    break;
print()
print('-='*25)
print()
print(f'Os número digitados foram ',end = '')
print(*dados,end = '...')

print(f'\nHá {len(dados)} números na lista.')
dados.sort(reverse=True)#fazer isso primeiro
print(f'Em ordem descrente {dados}')
if 5 in dados: #se o 5 esta na lista, printa
  print('O número 5 está na lista! ')
else: #se nao
  print('O número 5 não está na lista! ')