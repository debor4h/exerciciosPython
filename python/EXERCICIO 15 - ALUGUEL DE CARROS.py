dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos km rodados: '))
tot = (dias*60) + (km*0.15)
print('Pagar {} R$, por {} dias alugados e {:.2f}km percorridos.'.format(tot,dias,km))