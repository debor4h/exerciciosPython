altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))
area = altura*largura
pint = area/2
print('Altura de {:.2f}m com largura de {:.2f}m e a área de {:.2f}m².'.format(altura,largura,area))
print('{:.2f}L de tintas para pintar toda a área.'.format(pint))