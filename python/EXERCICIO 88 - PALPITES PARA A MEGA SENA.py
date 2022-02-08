#perguntar quantos jogos q que palpite ex 4,
#vai gerar 4 listas de 6 numeros
#a cada jogo tem um sleep
# de 1 a 60
#sample ele nao pega numeros repetidos
#codigo do aluno

from random import randint
from time import sleep
c =  cont = 0
a = int(input('Quantas palpites deseja: '))
for c in range(0,a):
    lista = []
    while len(lista) !=6:
        num = randint(0,60)
        if num not in lista: #se num nao estiver na lista
            lista.append(num)#adiciona ele na lista
    cont+=1
    print(f'Jogo {cont}º: {lista}')

#nao entendi, refazer