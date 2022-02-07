maior = menor = 0
lista = []
for pesos in range(1,5): #vai colocar os pesos dentro de pesos 4X
    peso = float(input(f'Qual seu peso, {pesos}º pessoa: ')) #aqui ele pergunta o peso e coloca o valor na variavel peso q vai p pesos
    lista.append(peso) #append coloca. Adicionar peso na lista
    if pesos == 1: #pesos na primeira posicao posicao vai receber o maior e o menor
        maior = peso
        menor = peso
    else: #se nao
        if peso>maior: #se o 2 peso  for maior q o primeiro pq e quem ele vai fazer a comparacao
            maior = peso #maior recebe esse peso
        if peso<menor: #se nao
            menor = peso # menor recebe esse peso

print(f'Maior peso: {maior :.2f}')
print(f'Menor peso: {menor :.2f}')

#forma com a lista
print(lista) #mostra a lista com tds os valores
print(f'Maior peso: {max(lista)}') #max pega o maior
print(f'Menor peso: {min(lista)}') #min pega o menor


#MAIOR E MENOR DOS PESOS LIDOS

#acumuladores
maior = 0
menor = 0

for pesos in range(1,6):
    peso = float(input("Informe seu peso, {}ª pessoa: ".format(pesos)))
    if pesos == 1:
        maior = peso  # De primeira tds recebem o primeiro peso
        menor = peso
    else:
        if peso > maior: #esse peso e o 2 valor que vai ser comparado com o primeiro peso
            maior = peso # se o 2 peso for maior que o primeiro MAIOR recebe 2 peso
        if peso < menor: #se o segundo peso for menor , que o menor q e o primeiro peso
            menor = peso #menor recebe o primeiro valor
print('-'*70)
print("O maior peso lido foi de {}".format(maior))
print("O menor peso lido foi de {}".format(menor))