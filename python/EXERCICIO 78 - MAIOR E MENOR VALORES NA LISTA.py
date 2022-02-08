#78 - ler 5 valores numericos e o maior e menor e suas posicoes
dados = list()
maior = menor = 0
for numeros in range(1,6):
  num = int(input(f'{numeros} º número: '))
  dados.append(num)
  if numeros == 1:
    maior = num
    menor = num
  else:
    if num>maior:
      maior = num
    if num<menor:
      menor = num

print(f'Todos os números da lista são: {dados}')
print(f'O maior número é : {maior} e sua posição é {dados.index(maior)+ 1}.')
print(f'O maior número é : {menor} e sua posição é {dados.index(menor)+ 1}.')