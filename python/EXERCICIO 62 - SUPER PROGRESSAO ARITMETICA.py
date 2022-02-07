#MELHORE O DESAFIO 61, PERGUNTE PARA O USUARIO QUANDO DE TERMSO ELE QUER MOSTRAR SE
#ELE DIGITAR 0 E PARA ACABAR O PROGRAMA
#pode ser pa decrescente ou crescente

a1 = int(input('Número inicial: '))#primeiro numero
r = int(input('De quantos em quantos deseja mostrar (RAZÃO): ')) #de quanto em quanto aumenta ou de quanto em quanto diminui
termo = int(input('Quantos números quer mostrar: '))
#formula da progressao aritmetica so utilizar quando ocorre soma entre os termos, soma iguais ,para
#numeros != ou mult nao mostrar
cont = 1
an = a1 + (termo-1)*r #esse -1 e da formula
for pa in range(a1,an + r,r): #ele nao ver como o limite 20, ele ver como se fosse ate o 20
    print(pa, end = ' ') #progressao aritmetica
    cont +=1
l=1
mais = 10
total = 0
while l !=0:
    total = total +l
    while cont<=total:
        termo+=r
        cont+=1
        l = int(input('\nQuantos termos você quer mostrar a mais: '))
        print(termo, end=' ')


#tentar resolver


#super progressao aritmetica
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
