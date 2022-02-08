#faca um programa que leia um numero e mostre o seu fatorial
#nao entendi

num = 1
numero = int(input('Informe um número para o fatorial: '))
dec = numero
print(f'{numero}! =',end = ' ')
for n in range (numero,0,-1):
    print(n,end = ' ')
    if n > 1:
      print('X',end = ' ')
    dec = n-1
    num *= dec+1
print(f' = {num}')
