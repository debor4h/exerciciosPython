#PC pensar em um numero entre 0 e 10,
#jogador vai ter q adivinhar ate acertar e mostrar quantas tentativas foram necessarias
from random import randint
tentivas = 1
pc = randint(0,10)
jogador = int(input('Em qual número o PC pensou....\nTente advinhar: '))
while jogador != pc:
    jogador = int(input('Em qual número o PC pensou....\nTente advinhar: '))
    tentivas +=1
    if jogador == pc:
        print(f'Parabéns, você acertou !\nO computador pensou no número {pc} e o jogador jogou o número {jogador}.')
print(f'Foram necessárias {tentivas} tentivas para acertar. ')


from random import randint
tentivas = 0
pc = randint(0,10)
acertou = False
while not acertou : #enquanto nao acertou
    jogador = int(input('Em qual número o PC pensou....\nTente advinhar: '))
    tentivas +=1
    if jogador>pc:
      print('Menos.. Tente mais uma vez.')
      acertou = False
    elif pc>jogador:
      print('Mais...Tente mais uma vez.')
      acertou = False
    elif jogador == pc:
      print(f'Parabéns, você acertou !\nO computador pensou no número {pc} e o jogador jogou o número {jogador}.')
      acertou = True
print(f'Foram necessárias {tentivas} tentivas para acertar. ')