produtos = ('Lápis',1.78,'Borracha',0.50,'Caderno',25.56,'Mochila',40.90,'Apontador',0.50,'Régua',5.67)
for i,v in enumerate(produtos):
    if i%2==0:
        print(f'{v:.<32}R$',end = '') #end coloca na msm linha
    elif i%2!=0:
        print(f'{v:.2f}') #para aparecer com 2 casas decimais
#.<32 ele ajusta o txt deixa centralizado, ele vai colocar os pontos



#vogais e consoantes
#tupla com varias palavras
#na palavra aprender temos as vogais a e e#lista com nome e o preco
#Borracha ............................ R$ 0.50

listagem = ('Pão', 1.00, 'Leite', 3.50, 'Frango', 10.90, 'Caderno', 24.56, 'Lápis', 2.50, 'Borracha', 0.50)
for l, i in enumerate(listagem):
    if l%2==0:
        print(f'{i:.<32}R$ ',end='')
    elif l%2!=0:
        print(f'{i}')

print('-'*45)
#75colocar o nome do produto e o preco
listagem = ('Pão',1,
            'Leite',3.50,
            'Frango',10.90,
            'Caderno',24.56,
            'Lápis', 2.50,
            'Borracha',0.50)
#Solucao comentario
for l in listagem:
    if type(l) is str:
        print(f'{l:.<32}',end = ' ')
    else:
        print(f'R${l:>5.2f}')
print('-'*45)
#solucao guanabara
#o nome sempre vai ta na posicao par
#e o valor sempre vai ta na posicao impar
for posicao in range(len(listagem)):
    if posicao %2==0:
        print(f'{listagem[posicao]:.<30}',end =' ')
    else:
        print(f'R$ {listagem[posicao]:>7.2f}')
#solucao dos comentarios um pouco confusa
print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(listagem), 2):
    print(f"{listagem[c]:.<40} R$ {listagem[c+1]:>7.2f}")

print("="*50)


#outro tipo p fazer
for cada in produtos:
  if type(cada) == str:
    print(f'{cada:.<30} ',end = ' ')
  else:
    print(f'R$ {cada :.2f}')