#poder ou nao formar um triangulo

print('='*25)

a = float(input('Digite o 1º segmento: '))
b = float(input('Digite o 2º segmento: '))
c = float(input('Digite o 3º segmento: '))

print('='*25)

if a+b>c and b+c>a and c+a>b:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')

print('='*25)