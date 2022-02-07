#78 - ler 5 valores numericos e o maior e menor e suas posicoes
valores = []
maior = menor = 0
for numeros in range(1,6):
    n = (int(input('Digite os valores: ')))
    valores.append(n)
    if numeros == 1:
        maior =n
        menor =n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Maior valor é {maior} nas posições ',end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'Menor valor é {menor} nas posições ',end='')
for i,v in enumerate(valores):
    if v==menor:
        print(f'{i}...',end='')




#pedir 5 valores, maior e menor e a sua posicao
maior=menor= 0
valores = []
for valor in range(1,6):
    #adicionando os valores digitados dentro da lista
    valores.append(int(input(f'{valor}ª valor: ')))
#c e contador e v e valor
for c,v in enumerate(valores):
    if c == 0: #se c for == a 0
        maior = v #maior e menor recebe o primeiro valor
        menor = v
    else:#se nao, ele vai ficar nesse looping
        if v>maior: #se v(novo) valor for maior que o valor 0
            maior=v #ele entrara nessa variavel
            posmaior = c
        if v<menor: #se nao
            menor=v


print('-'*70)
print(f'Todos os números digitados foram {valores}')
print(f'Maior número é o {maior} na posição ',end ='')
for indice, val in enumerate(valores):
    if val == maior:
        print(f'{indice}',end =' ')
print()#aqui e para pular linha
print(f'Menor número é o {menor} na posição ',end ='')
for indice, val in enumerate(valores):#enumerate ele pega o valor e o indice
    if val == menor:
        print(f'{indice}',end = ' ')
print()
print('-'*70)

lista = []
for laco in range(1,6):
        lista.append(int(input(f'Digite o {laco}º valor: ')))
print('-'*70)
max = max(lista)
min = min(lista)
print(f'Os valores digitados foram: {lista}')
print(f'Maior valor: {max} na posição {lista.index(max)}.')
print(f'Menor valor: {min} na posição {lista.index(min)}.')


#78 - ler 5 valores numericos e o maior e menor e suas posicoes
dados = list()
maior = menor = 0
for numeros in range(1,6):
  num = int(input(f'{numeros} º número: '))
  dados.append(num)
  if numeros == 1:
    maior = num
    menor = num
  else:
    if num>maior:
      maior = num
    if num<menor:
      menor = num

print(f'Todos os números da lista são: {dados}')
print(f'O maior número é : {maior} e sua posição é {dados.index(maior)+ 1}.')
print(f'O maior número é : {menor} e sua posição é {dados.index(menor)+ 1}.')