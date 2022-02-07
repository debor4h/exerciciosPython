import random,time #importando
print(' ***************** Sorteando número ***************** ')
n = random.randint(0,5) #RANDOM E PARA O COMPUTADOR GERAR NUMERO
num = int(input('Digite um número entre 0 e 5: '))
if n == num:
    print('Venceu')
else:
    print('Perdeu')
print('Número sorteado: {}'.format(n))



pc = random.randint(0,5)#sorteando um numero entre 0 e 5

#\033[1;35m \033[m codigo de cor, 1 e o stylo e 35m e a cor, o m vem antes da frase, separados por ; deixar a frase junto para nao ter espacos

print('\033[1;35m= \033[m'*27)
print('\033[1;31mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;34m= \033[m'*27)

jogador = int(input('Em que número pensei? '))
print('\033[1;36mPROCESSANDO...\033[m')
time.sleep(2) #tempo de 2 segundos, para mostrar o resultado
if jogador != pc: #se pc for diferente de jogador
  print(f'\033[1;33mGANHEI! Eu pensei no número {pc} e não no {jogador} !\033[m')
else: #se ambos forem iguais
  print(f'\033[1;33mPARABÉNS! Você conseguiu me vencer!\033[m')