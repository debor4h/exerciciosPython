preco = float(input('Digite o preço do produto: '))
desc = preco - ((preco*5)/100)
print('Com 5% de desconto o valor do produto foi para R${:.2f}'.format(desc))