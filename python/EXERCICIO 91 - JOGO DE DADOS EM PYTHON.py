#4 JOGADOR JOGA UM DADO ENTRE 1 E 6
#GUARDE EM UM DICIONARIO
#E COLOCAR EM ORDEM DO MAIOR AO MENOR Nº SORTEADO
#TEM SLEEP
#O JOGADOR1 TIROU 4
#O JOGADOR2 TIROU 6

#solucao guanabara
from random import randint
from time import sleep
from operator import itemgetter
dic = {'jogador1':randint(1,6),
       'jogador2':randint(1,6),
       'jogador3':randint(1,6),
       'jogador4':randint(1,6)}
r = list()
print('Sorteando Valores')
for k,v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    #itemgetter
    #key e chave
    #0 e cheve
    #1 e valor
r = sorted(dic.items(),key=itemgetter(1),reverse= True)
print('-='*30)
print('===== RANKING =====')
for i,v in enumerate(r):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')

#minha solucao


#4 JOGADOR JOGA UM DADO ENTRE 1 E 6
#GUARDE EM UM DICIONARIO
#E COLOCAR EM ORDEM DO MAIOR AO MENOR Nº SORTEADO
#TEM SLEEP
#O JOGADOR1 TIROU 4
#O JOGADOR2 TIROU 6
from random import randint
from time import sleep
from operator import itemgetter
dic = {}

for laco in range(1,5):
    dic['jogador'] = randint(1,6)
    for i,v in dic.items():
        print(f'{i}{laco} tirou {v} no dado.')
        sleep(1) #para dar um tempo apar ele mostrar

    ranking = sorted(dic.items(),key=itemgetter(1),reverse= True)
    print('===== RANKING =====')
