#e igual ao 86 que tem q criar uma matriz 3x3
#soma dos valores pares
#a soma dos valores da 3 coluna
#o maior valor da 2 linha e
soma=pares=maior=0
m = [[0,0,0,],[0,0,0,],[0,0,0,]]
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f'Digite o número {[l],[c]}: '))
print('-='*50)
for li in range(0,3):
    for co in range(0,3):
        #:^5 cinco espacos centralizados
        print(f'[{m[li][co]:^5}]', end='')
        if m[li][co] %2==0: #vendo se é par
            pares += m[li][co]
    print()
print('-='*50)
print(f'A soma dos números pares são: {pares}')
#coluna fixa linha variavel
for l in range (0,3):
    soma+=m[l][2]
print(f'A soma dos números da terceira coluna são: {soma}')
for c in range(0,3):
  if c == 0:
      maior = m[1][c]
  elif m[1][c] > maior:
      maior = m[1][c]
print(f'O maior valor da segunda coluna é: {maior}')

#nao entendi