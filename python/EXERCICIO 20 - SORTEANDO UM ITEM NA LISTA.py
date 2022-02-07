#ordem dos que vao apresentar
import random # SORTEAR
a = str(input('1º nome: '))
b = str(input('2º nome: '))
c = str(input('3º nome: '))
d = str(input('4º nome: '))
l = [a,b,c,d] #lista l é tipo um vetor, colocou os nomes em uma lista

#para o shuffler funcionar a lista tem q estar em []
random.shuffle(l) #shuffle significa embaralhar a lista (l)
print(' ************** Ordem da apresentação ************** ')
print(l) #ele vai apresentar a lista td embaralhada