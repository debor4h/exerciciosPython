from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
tot = venceu = 0
computador = randint(0, 10) #ele vai ate o 10
p = 'PAR'
i = 'ÍMPAR'
while True:
        num = int(input('Diga um valor: '))#jogador
        op = ' ' #iniciando ja que e string tem q colocar entre ' '
        #aqui fica num loop infinito ate digitar o certo
        while op not in 'PpIi': #enquanto op nao for P ou p ou I ou i nao vai validar, ele ficara repetindo isso
            op = str(input('Par ou Ímpar [P|I]? ')).strip().upper()
        tot = computador + num
        print('=-' * 15)
        print(f'Você jogou {num} e o computador {computador}.', end=' ')
        if tot%2==0:
            if op == 'P':
                print(f'Total de {tot} DEU {p}')
                venceu +=1
                print('Você GANHOU!')
            if op == 'I':
                print(f'Total de {tot} DEU {p}')
                print('Você PERDEU!')
                break; #para quebrar o laco
        elif tot%2!=0:
            if op == 'P':
                print(f'Total de {tot} DEU {i}')
                print('Você Perdeu!')
                break;  # ele interrompe o bloco e ja vai para o final, continuando
            if op == 'I':
                print(f'Total de {tot} DEU {i}')
                venceu += 1
                print('Você GANHOU!')
        print('Vamos jogar novamente....')
print('=-' * 15)
print(f'GAME OVER! Você venceu {venceu} vezes.')
print('=-' * 15)

from random import randint #importando o random

pc = randint(0,9) #de 0 a 9
cont = soma = vitoria = 0

while True: #enquanto for verdade, looping infinito
  jogador=int(input('Qual sua aposta?...\nDigite um número:  '))#jogar o numero
  parImpar = ' '#validando para  receber apenas P ou I
  while parImpar != 'P' and parImpar !=  'I':
    parImpar=str(input('Par ou Ímpar:  ')).upper().strip()
  soma = jogador + pc #soma entre os numeros
  if (soma%2==0) and (parImpar == 'P'): #se o resultado modulo for 0 e escolheu PAR
      print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}, DEU PAR.')
      print('Você ganhou !')#ele ganhou
      cont+=1#para contar quantas vezes venceu
  elif (soma%2!=0) and (parImpar == 'I'):
      print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}, DEU ÍMPAR.')
      print('Você ganhou !')
      cont+=1 #para contar quantas vezes venceu
  elif (soma%2==0) and (parImpar == 'I'):
      print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}, DEU PAR.')
      print('Você PERDEU !')
      break;#aqui ele para é o flag
  elif (soma%2!=0) and (parImpar == 'P'):
      print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}, DEU ÍMPAR.')
      print('Você PERDEU !')
      break; #flag
print('*'*45)
print(f'GAME OVER, você venceu {cont} vezes.')