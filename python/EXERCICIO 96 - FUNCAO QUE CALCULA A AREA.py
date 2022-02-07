def area(msg):#declaracao da funcao com o parametro msg
   print(msg)#aqui msg e a area


print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(f'A área do seu terreno {l}X{c} é de {l*c}m².')
