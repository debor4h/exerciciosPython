#ler 4 valores pelo teclado e colocar em uma tupla
#quantas vezes aparece 9
#em q posicao foi digitado o primeiro 3
#numeros pares
numeros = ()
pares = ()

n1=int(input('Digite o 1º número: '))
n2=int(input('Digite o 2º número: '))
n3=int(input('Digite o 3º número: '))
n4=int(input('Digite o 4º número: '))

numeros = (n1,n2,n3,n4)
print(numeros)
if 9 in numeros:
    print(f'O número 9 aparace {numeros.count(9)}X na tupla.')
elif 9 not in numeros:
    print(f'O número 9 não aparace na tupla. ')
if 3 in numeros:
    print(f'O número 3 aparace na posição(ções): ',end = ' ')
    for i,v in enumerate(numeros):
        if v == 3:
            print(f'{i}....',end='')
elif not 3 in numeros:
    print('O número três não está na tupla.')
print()
print('Os valores pares foram:', end =' ')
for v in numeros:
    if v%2==0:
        pares = v
        print(f'{pares}....',end = ' ')

