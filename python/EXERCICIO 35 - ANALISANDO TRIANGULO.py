#poder ou nao formar um triangulo

print('='*25)#aqui ele vai repetor esse sinal 20 vezes

a = float(input('Digite o 1º segmento: '))
b = float(input('Digite o 2º segmento: '))
c = float(input('Digite o 3º segmento: '))

if a+b>c and b+c>a and c+a>b:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')

print('-='*25)
print('Analisador de Triângulo')
print('-='*25)

a1 = float(input('1º segmento: '))
b1 = float(input('2º segmento: '))
c1 = float(input('3º segmento: '))

#abs ele troca o sinal do numero para mais
# valor absoluto (módulo) sempre sera positivo
if (abs(b1-c1)<a1<b1+c1) and (abs(a1-c1)<b1<a1+c1) and (abs(a1-b1)<c1<a1+b1):
  print('Os segmentos acima PODEM FORMAR um triângulo! ')
else:
   print('NÃO PODEM FORMAR um triângulo! ')
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b