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

#75
nove  = pares = 0

n1 = int(input('Digite os valores: '))
n2 = int(input('Digite os valores: '))
n3 = int(input('Digite os valores: '))
n4 = int(input('Digite os valores: '))
numeros = (n1,n2,n3,n4)
print('-'*50)
print(f'Você digitou os valores {numeros}')
if numeros[0]== 3 or numeros[1]== 3 or numeros [2]== 3 or numeros [3]== 3:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'Os valores pares foram: ',end=' ')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')

#solucao guanabara
#aqui ele esta dentro de uma tupla pq esta entre ()
num= (int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')))
print('-'*50)
print(f'Os valores digitados foram: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num: #se 3 esta em num
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')#+1 pq comeca do zero ai o primeiro tem q ser um
else:
    print('O valor 3 não foi digitado')
print('Os valores pares foram:', end =' ')
for n in num:#para n no num
    if n%2==0:
        print(n,end=' ')

#outra forma
valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')