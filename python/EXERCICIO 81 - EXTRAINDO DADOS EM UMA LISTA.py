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