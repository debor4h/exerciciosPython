#faca um programa que leia um numero e mostre o seu fatorial
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



#faca um programa que leia um numero e mostre o seu fatorial
num = 1

numero = int(input('Informe um número para o fatorial: '))
n = numero
print(f'{numero}! = ',end ='')
while numero>0:
  print(numero,end ='')
  numero-=1 #aqui ele vai tirar 1, vai do 5 até chegar no 1
  if numero>=1: #vai printar os X
    print(' X ',end = '')
  num  *= numero+1
 # exemplo com 5
  #1 = 1*1=1
  #1 = 1 * 2 = 2
  #2 = 2 * 3 = 6
  #6 = 6 * 4 = 24
  #24 = 24 * 5 = 120


print(f' = {num}')


#Modo tradicional
n = int(input('Digite um número: '))
c = n # fatorial comeca com n que e o numero que vc digitou
fator = 1 #para a multiplicar fica impar
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c), end = '')
    print('X' if c >1 else '=',end = '')
    fator = fator *c
    c-=1
print('{}'.format(fator))
