import math #importação da biblioteca de matematica
num = int(input('Digite um número: '))
dobro = num*2
triplo = num*3
rq = math.sqrt(num)
print('Dobro: {}\nTriblo: {}\nRaiz Quadrada: {:.2f}'.format(dobro,triplo,rq))

print('*'*45)
#dessa forma nao precisa importar a biblioteca
raiz = num**(1/2)
print('Raiz Quadrada: {:.2f}'.format(raiz)) #aqui já faz direto
print('Dobro: {:.2f}'.format(num*2))
print('Triplo: {:.2f}'.format(num*3))