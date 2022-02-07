#071)Simular caixa eletronico, celulas 50,20,10,1 R$.EX: 100 e duas celulas de 50
#FORMA SEM O WHILE
saque = float(input('Qual valor você quer sacar? R$ '))
if saque == 0 or saque < 0:
  print('Digite um valor acima de ZERO, por favor!')

cinquenta = saque//50
vinte = (saque%50)//20
dez = ((saque%50)%20)//10
um = ((saque%50)%10)

print(f'Total de {cinquenta} células de R$50')
print(f'Total de {vinte} células de R$20')
print(f'Total de {dez} células de R$10')
print(f'Total de {um} células de R$1')



#nao conseguir entender essa logica do guanabara
print('*'*45)
print(f'Banco DEV')
print('*'*45)
valor = float(input('Qual valor você quer sacar? R$ '))
tot = valor
ced = 50 #vai comecar com a de  maior valor no eninciado
totcedula = 0
while True:
  #quantas vezes eu consigo tirar 50 do total
    if tot>=ced:
      tot -= ced
      totcedula +=1
    else:
      if totcedula > 0:
        print(f'Total de {totcedula} cédulas é de R$ {ced}')
      if ced == 50:
        ced = 20
      elif ced == 20:
        ced = 10
      elif ced == 10:
        ced = 1
      totcedula = 0
      if tot == 0:
        break;
