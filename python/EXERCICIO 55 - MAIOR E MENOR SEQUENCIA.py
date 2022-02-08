maior = menor = 0
lista = []
for pesos in range(1,5):
    peso = float(input(f'Qual seu peso, {pesos}º pessoa: '))
    lista.append(peso) #adicionar peso na lista
    if pesos == 1: #pesos na primeira posicao vai receber o maior e o menor
        maior = peso
        menor = peso
    else:
        if peso>maior: #se o 2 peso for maior q o primeiro
            maior = peso #maior recebe esse peso
        if peso<menor: #se nao
            menor = peso # menor recebe esse peso

print(f'Maior peso: {maior :.2f}')
print(f'Menor peso: {menor :.2f}')

#outra forma com a lista
#print(lista) #mostra a lista com tds os valores
#print(f'Maior peso: {max(lista)}') #max pega o maior
#print(f'Menor peso: {min(lista)}') #min pega o menor
