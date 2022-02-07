#nao entendi
#matriz 3x3
matriz =[[0,0,0],[0,0,0],[0,0,0]] #vai ter 3 valores dentro de cada listas
for linha in range(0,3):
  for coluna in range(0,3):
    matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
print('-='*14)
# para mostrar
for linha in range(0,3):
  for coluna in range(0,3):
    print(f'[{matriz[linha][coluna]:^5}]',end ='')   #:^5 cinco espacos centralizados
  print()#para quando chegar em 3 no for ele printa na linha de baixo, quebrar linha