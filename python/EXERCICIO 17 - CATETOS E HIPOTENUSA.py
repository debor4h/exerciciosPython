#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retangulo.Calcule e mostre o comprimento da hipotenusa
import math
cO = float(input('Digite o cateto oposto: '))
cA = float(input('Digite o cateto adjacente: '))
x = (cO**2)+(cA**2)

#outra forma de fazer
h = math.hypot(cO,cA) #CALCULANDO A HIPOTENUSA
print('Resultado deu {:.1f}'.format(math.sqrt(x)))#SQRT E RAIZ QUADRADA

print('Resultado deu {:.1f}'.format(h))

