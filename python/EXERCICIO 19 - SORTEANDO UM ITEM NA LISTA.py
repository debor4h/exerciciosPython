#quem vai apagar o quadro
from random import choice #AQUI VAI SORTEAR
a = str(input('Digite 1º nome: '))
b = str(input('Digite 2º nome: '))
c = str(input('Digite 3º nome: '))
d = str(input('Digite 4º nome: '))
lista = [a,b,c,d]

es = choice(lista) #CHOICE SORTEA
print('Escolhido(a) foi {}.'.format(es))

#sorted() embaralha