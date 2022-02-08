#gerar 5 valores aleatorios
#colocar em tupla
#maior e menor

valores = ()
maior = menor = 0
from random import randint

for cinco in range(1,6):
    valores=(randint(0,100))
    print(valores,end = ' ')
    if cinco == 1:
        maior = valores
        menor = valores
    if valores > maior:
        maior = valores
    if valores< menor:
        menor = valores
print()
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print() #pular linha
