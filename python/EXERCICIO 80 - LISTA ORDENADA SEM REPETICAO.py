#5 valores colocar em uma lista
#nao pode usar o sort
#colocar os valores em ordem numerica
#adicionado na posicao 0 o numero 2
#pedi outro valor

numeros = []
for c in range(0,5):
    n =int(input('Digite os valores: '))
    if c == 0:
        numeros.append(n)#se for o primeiro valor add
    #pegando o ultimo elemento da lista numeros[len(numeros)-1] ou numeros[-1]
    #se n for maior que o ultimo elemnto da lista
    elif n>numeros[len(numeros)-1]:
        numeros.append(n)
    else:
        pos = 0
        #enquanto pos que e 0 for menor que o tamanho da lista
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos,n)
                break;
            pos+=1
print('*='*30)
print(f'Os valores digitados em ordem foram {numeros}')
print('*='*30)

