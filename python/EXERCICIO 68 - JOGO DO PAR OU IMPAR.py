from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
tot = venceu = 0
computador = randint(0, 10)
p = 'PAR'
i = 'ÍMPAR'
while True:
        num = int(input('Diga um valor: '))
        op = ' '
        while op != 'P' and op != 'I':
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
                break;
            if op == 'I':
                print(f'Total de {tot} DEU {i}')
                venceu += 1
                print('Você GANHOU!')
        print('Vamos jogar novamente....')
print('=-' * 15)
print(f'GAME OVER! Você venceu {venceu} vezes.')
print('=-' * 15)