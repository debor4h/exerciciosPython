#MELHORE O DESAFIO 61, PERGUNTE PARA O USUARIO QUANDO DE TERMSO ELE QUER MOSTRAR SE
#ELE DIGITAR 0 E PARA ACABAR O PROGRAMA

#tentar resolver

a1 = int(input('Qual o primeiro termo (a1): '))
r = int(input('Qual a razão (r): '))
contador = 1
limite_Inicial= 10

while contador <=limite_Inicial:
  a1+=r
  print(a1,end = ' -> ')

  contador+=1
  if contador>=limite_Inicial:
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
    if mais >0:
      limite_Inicial +=mais
    elif mais == 0:
      limite_Inicial +=mais
      break;
print(f'Progressão finalizada com {limite_Inicial} termos mostrados.')
