from datetime import date
ano = int(input('Em que ano você está, 0 para o ano atual: '))

#condicao simples, so com um if
if ano == 0:
   ano = date.today().year #pega o ano atual

#condicao composta
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('ANO BISSEXTO: ')
else:
    print('ANO NÃO BISSEXTO {}'.format(ano))
    #ano bissexto e a cada 4 anos

#Divisível por 4. A divisão é exata com o resto igual a zero;

#Não pode ser divisível por 100. Com isso, a divisão não é exata,
#ou seja, deixa resto diferente de zero;

#Caso seja divisível por 400 a divisão deve ser exata, deixando o resto igual a zero.