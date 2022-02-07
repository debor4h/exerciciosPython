#quem vai apagar o quadro
from random import choice #AQUI VAI SORTEAR
a = str(input('Digite 1º nome: '))
b = str(input('Digite 2º nome: '))
c = str(input('Digite 3º nome: '))
d = str(input('Digite 4º nome: ')) #str é para palavra, colocar se nao podera ir números
lista = [a,b,c,d] #LISTA E TIPO UM VETOR
#escolher um valor entre os quatro

#quando importa o from import nao colocar math na frente de choice
es = choice(lista) #CHOICE SORTEA
print('Escolhido foi {}'.format(es))

#sorted() embaralha