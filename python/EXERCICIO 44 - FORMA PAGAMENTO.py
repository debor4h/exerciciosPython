print(f'{ "LOJAS GUANABARA ":=^50}') #dessa forma nao precisa criar uma var para loja
produto = float(input("Valor do produto: "))
print('-'*50)
opcoes = int(input("1 - Á vista no dinheiro ou cheque 10% de desconto.\n2 - Á vista no cartão com 5% de desconto.\n3 - 2x no cartão preço normal.\n4 - 3x ou mais no cartão 20% de juros.\nInforme a opção desejada: "))
print('-'*50)
if (opcoes == 1) :
    op = int(input("1 para Dinheiro ou 2 para Cheque: "))
    if(op == 1):
        print('-' * 50)
        print("Forma de pagamento em dinheiro, valor ficou {} com 10% de desconto.".format(produto-((produto*10)/100)))

    else:
        print("Pagamento feito em cheque com 10% de desconto, valor foi para {}".format(produto - ((produto*10)/100)))
elif(opcoes == 2):
   print("Á vista com 5% de desconto, valor ficou {}".format(produto - ((produto*5)/100)))
elif(opcoes == 3):
    print("2X no cartão, {}".format(produto/2))
elif(opcoes == 4):
    b = int(input("Quantas vezes no cartão: "))
    print('-'*50)
    if (b>=3):
        print("3X ou mais no cartão 20% de juros, valor ficou {}".format((produto + ((produto*20)/100))/b))
        print("Valor total da compra com juros {}".format((produto + ((produto*20)/100))))
    else:
        print("Opção inválida !!!")
else:
    print("Opção inválida !!!")