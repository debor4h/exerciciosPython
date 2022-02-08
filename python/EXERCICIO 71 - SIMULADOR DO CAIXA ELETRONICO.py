#071)Simular caixa eletronico, celulas 50,20,10,1 R$.EX: 100 e duas celulas de 50
#FORMA SEM O WHILE
saque = float(input('Qual valor você quer sacar? R$ '))
if saque == 0 or saque < 0:
  print('Digite um valor acima de ZERO, por favor!')

cinquenta = saque//50
vinte = (saque%50)//20
dez = ((saque%50)%20)//10
um = ((saque%50)%10)

print(f'Total de {cinquenta :.2f} células de R$50')
print(f'Total de {vinte  :.2f} células de R$20')
print(f'Total de {dez  :.2f} células de R$10')
print(f'Total de {um  :.2f} células de R$1')


