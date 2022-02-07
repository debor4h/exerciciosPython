from random import randint # importcao do randint
from time import sleep #importacao do sleep
numeros = list() #criacao da lista
def sorteia():#declaracao da funcao
    print('Sorteando 5 valores da lista: ')
    for sorteando in range (1,6):#sorteando 5 valores
        num = randint(1,100) #colocando os valores em num que sera colocado em sorteando
        numeros.append(num)#adicionando os valores na lista
        sleep(0.5)#tempo de 0.5 entre 1 e o outro para printar
        print(num,end=' ')#valores um do lado do outro
    print()#pular linha

#programa principal
sorteia()

def somaPar():#funcao
    soma = 0#soma
    for c in numeros:#laco p percorrer a lista numeros
        if c % 2 == 0:#se c que sao os numeros modulo de 2 for igual a 0
            soma+=c#somalos
    print(f'Somando os valores pares de {numeros}, temos {soma}')#printar

#programa principal
somaPar()#mostrar