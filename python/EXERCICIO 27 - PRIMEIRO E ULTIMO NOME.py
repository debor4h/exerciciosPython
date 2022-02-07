#FACA UM PROGRAMA QUE INFORME O PRIMEIRO E ULTIMO NOME
#nome=str(input('Digite seu nome completo: ')).upper().strip()
#n = nome.split()
#print('Seu primeiro nome é: {}'.format(n[0]))
#print('Seu último nome é: {} '.format(n[len(n)-1])) # o len vai contar os split que sao divididos
#split comeca do zero e o len do 1, entao o menos 1 e para igualar ao split
#nesse -1 é pq e o final se tivesse 3 blocos a primeira letra ia ser -3..

name = str(input('Digite seu nome completo: ')).upper().strip()
print('Seu primeiro nome é: {}'.format(name.split()[0]))
print('Seu último nome é: {}'.format(name.split()[-1]))


































