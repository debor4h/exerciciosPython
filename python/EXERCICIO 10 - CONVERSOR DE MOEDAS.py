real = float(input('Quanto dinheiro possuí na carteira R$: '))
dolares = real/5.26 #convertendo para real
print('Com R${} é possível comprar US${:.2f} '.format(real,dolares))