#ordem dos que vao apresentar
import random # SORTEAR
a = str(input('1º nome: '))
b = str(input('2º nome: '))
c = str(input('3º nome: '))
d = str(input('4º nome: '))
lista = [a,b,c,d]

#para o shuffler funcionar a lista tem q estar em []
random.shuffle(lista) #shuffle significa embaralhar a lista (lista)
print(' ************** Ordem da apresentação ************** ')
print(lista) #ele vai apresentar a lista td embaralhada