#tupla com contagem de 0 a 20
#ler no teclado um numero de 0 a 20 e mostrar em txt
#repetir ate o numero ser maior q zero e menor ou igual a 20


#tuplas com os numeros entre 0 e 20
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
         'nove','dez','onze','doze','treze','quatorze','quinze','desesseis','dezesete','dezoito','dezenove','vinte')


while True:
    num = int(input('Digite um número entre 0 e 20: '))#pergunte
    if 0 <= num <=20:
        break;
    print('Tente novamente....')

for cont in range(0,len(tupla)):
    if cont == num:
        print(f'Você digitou o número {tupla[cont]}')



