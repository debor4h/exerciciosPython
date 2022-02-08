#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno
#cosseno e tangante
import math

x = float(input('Digite o ângulo que você deseja calcular: '))
seno = math.sin(math.radians(x)) # vai pegar o seno e converter para radianos
print('Ângulo de {} tem SENO de {:.2f}'.format(x,seno))
cosseno = math.cos(math.radians(x))
print('Ângulo de {} tem SENO de {:.2f}'.format(x,cosseno))
tangente = math.tan(math.radians(x))
print('Ângulo de {} tem TANGENTE de {:.2f}'.format(x,tangente))
#radians faz uma conversao