#5 valores colocar em uma lista
#nao pode usar o sort
#colocar os valores em ordem numerica
#adicionado na posicao 0 o numero 2
#pedi outro valor
numeros = []
for c in range(0,5):
    n =int(input('Digite os valores: '))
    if c == 0:
        numeros.append(n)#se for o primeiro valor add
    #pegando o ultimo elemento da lista numeros[len(numeros)-1] ou numeros[-1]
    #se n for maior que o ultimo elemnto da lista
    elif n>numeros[len(numeros)-1]:
        numeros.append(n)
    else:
        pos = 0
        #enquanto pos que e 0 for menor que o tamanho da lista
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos,n)
                break;
            pos+=1
print('*='*30)
print(f'Os valores digitados em ordem foram {numeros}')
print('*='*30)


#80 - usuario digita 5 valores numericos, e coloca em ordem, nao usar o sort.
lista = list()
num = 0
for n in range(1,6):
  numero = int(input(f'Digite o {n}º número: '))
  if n == 1:
    lista.append(numero) #se for o 1 valor adicionar na lista
  elif numero>lista[len(lista)-1]: #para pegar o ultimo elemento, se o numero for maior q o ultimo elemento
    lista.append(numero)
  else:
    pos = 0 #posicao
    while pos<len(lista): #enquanto posicao for menor q o tamanho da lista
      if numero<=lista[pos]:#se numero for menor ou igual a lista na posicao pos
        lista.insert(pos,numero)
        break;
      pos+=1

print(lista)


from matplotlib import pyplot as plt
x = []
y = []
for i in range(100):
    if i != 0:
        if 100/i != 1:
            x.append(i)
            y.append(x[i-1]**2)
plt.plot(x, y)
plt.show()


s = "Python top!"
i = 0
while i != len(s):
    i += 1
    print(s[-i])


for j in range(len(s)):
    print(s[-j - 1])