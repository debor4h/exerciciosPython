#leia um numero de 0 a 9999 e mostre cada um dos dígitos separados M C D U
n = int(input('Informe um número: '))
u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
#nao entendi muito


#leia um numero de 0 a 7777 e mostre cada um dos dígitos separados M C D U

#validando
while True:
  numero = int(input('Digite um número entre 0 - 7777: '))
  if numero < 7777:
    break;

print(f'Analisando o número {numero}')
#% modulo (resto)
#// divisao inteira (embaixo da chave)
unidade =(numero%10)
dezena = (numero%100)//10
centena = (numero%1000)//100
milhar = (numero%10000)//1000

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')


#Com fatiamento, passar para string e acessar pelos indices