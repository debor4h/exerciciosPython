#gerar 5 valores aleatorios
#colocar em tupla
#maior e menor

valores = ()
maior = menor = 0
from random import randint

for cinco in range(1,6):
    valores=(randint(0,100))
    print(valores,end = ' ')
    #nao colocar valores[0] pq ele so vai considerar esse numero e os demais nao, vai dar erro
    if cinco == 1:
        maior = valores
        menor = valores
    if valores > maior:
        maior = valores
    if valores< menor:
        menor = valores
print() #pular linha
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print() #pular linha
#importar 5 numeros aleatorios e mostrar o maior e menor valor
import random
maior = menor = 0
for laco in range(0,5):
    n = random.randint(0,100)
    print(n, end =' ')
    if laco == 1:
        maior = n
        menor = n
    else:
        if n>maior:
            maior = n
        if n<menor:
            menor = n
print('\n')
print('-'*80)
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print('\n')
print('-'*80)
#outra forma de fazer, aqui colocou entre () para ficar dentro da tupla
n1 = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),
     random.randint(1,10),random.randint(1,10))
for num1 in n1:#para cada num1 em n1
    print(f'{num1}',end =' ')#mostra
print(f'\nMaior valor: {max(n1)}')
print(f'Menor valor: {min(n1)}')
print('\n')
print('-'*80)
#Outra forma de faze
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')


from random import randint

c =maior=menor=0
while c<5:
  numeros = (randint(0,100)) # colocando () ele ja considera tupla
  c+=1
  if c == 1:
    maior = numeros
    menor = numeros
  else:
    if numeros>maior:
      maior=numeros
    if numeros<menor:
      menor=numeros
  print(numeros, end = ' ')
print()
print(f'O maior número: {maior}')
print(f'O menor número: {menor}')


#outra forma

a = tuple(randint(1,10) for i in range(5))
print(a)
print(max(a))
print(min(a))


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
