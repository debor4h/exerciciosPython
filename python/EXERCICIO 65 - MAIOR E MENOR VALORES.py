#65 - maior ou menor,varios numeros e mostrar a media,
#perguntar ao usuarios se quer ou nao continuar

maior = menor = media = cont = 0
laco = 'S'
while laco == 'S':
    n1 = int(input('Digite os valores: '))
    cont +=1
    if cont == 1: #se contador for igual a 1, ou seja a primeira vez q ele conta o primeiro numero
        maior = n1
        menor = n1
    else: # se o segundo numero for maior q o primeiro
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    media = n1 + media
    laco = ' '
    while laco != 'S' and laco != 'N':
        laco = str(input('Deseja continuar [S|N]: ')).upper().strip()
    if laco != 'S':
        print('Programa finalizado.')
print('-'*100)
print('A média foi de: {:.2f}'.format(media/cont))
print('Maior número foi: {}'.format(maior))
print('Menor número foi: {}'.format(menor))
