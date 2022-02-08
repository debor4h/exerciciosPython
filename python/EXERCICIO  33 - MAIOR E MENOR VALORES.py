#Obtive dúvida
n = int(input('Digite o 1º número: '))
u = int(input('Digite o 2º número: '))
m = int(input('Digite o 3º número: '))

num = [n,u,m]
#esse max ele organiza a lista do menor para o maior, pegar -1 pega o da direita o maior
print('Maior {}'.format(max([num][-1])))
print('Menor {}'.format(min([num][0])))

#ou

print('**************************************************')

lista = [n,u,m]
listaOrdenada = sorted(lista) #sorted faz com q os numeros fiquem em ordem crescente
print('Maior: ',listaOrdenada[-1])
print('Menor: ',listaOrdenada[0])

#ou

print('**************************************************')

menor = n

if u<n and u<m:
    menor = u
if m<n and m<u:
    menor = m

maior = n
if u>n and u>m:
    maior = u
if m>n and m>u:
    maior = m

print('Guanabara Maior {}'.format(maior))
print('Guanabara Menor {}'.format(menor))


