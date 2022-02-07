#tupla com contagem de 0 a 20
#ler no teclado um numero de 0 a 20 e mostrar em txt
#repetir ate o numero ser maior q zero e menor ou igual a 20
numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete'
           ,'dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 0 and num <=20:
        break;
for indice, valor in enumerate(numeros):
    if num == indice:
        print(f'{valor}')


#tuplas com os numeros entre 0 e 20
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
         'nove','dez','onze','doze','treze','quatorze','quinze','desesseis','dezesete','dezoito','dezenove','vinte')


#while num > 20 or num < 0:#enquanto numero for maior ou menor que zero
while True:
    num = int(input('Digite um número entre 0 e 20: '))#pergunte
    if 0 <= num <=20:
        break;
    print('Tente novamente....')  # pergunte

for cont in range(0,len(tupla)):
    if cont == num: #se cont for igual a num
        print(f'Você digitou o número {tupla[cont]}')#vc digitou o numero tupla no cont

#cont sao os numeros que representam as letras



#072)uma tupla com numeros de 0 a 20(escrito), seu programa devera ler um numero pelo teclado (0-20) e exibi-lo por extenso Validar o intervalo.

#tupla criada
numeros= ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:#looping infinito
  num=int(input('Digite um número entre (0-20): '))
  if num >= 0 and num <=20:# se numero for maior ou igual a zero e menor ou igual a 20
    #para dado no intervalo de quantidade de numeros
    for dado in range(0, len(numeros)):
      if dado == num: #se dado que vai contar for igual ao numero digitado
        print(f'O número digitado foi: {numeros[dado]}')#escrever por extenso
  #validando
  op = ' '
  while op != 'S' and op != 'N':
    op = str(input('Deseja continuar[S|N]: ')).upper()
  if op == 'N': #se for igual a nao, pare
    break;
