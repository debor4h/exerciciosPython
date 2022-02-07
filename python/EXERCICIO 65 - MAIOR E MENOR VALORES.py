#65 - maior ou menor,varios numeros e mostrar a media,
#perguntar ao usuarios se quer ou nao continuar
maior = menor = media = cont = 0
laco = 'S' #resposta
while laco == 'S':
    n1 = int(input('Digite os valores: '))
    cont +=1
    if cont == 1: #se contador for igual a 1, ou seja a primeira vez q ele conta o primeiro numero
        maior = n1  #De primeira tds recebem o msm valor
        menor = n1
    else: # se o segundo numero for maior q o primeiro
        if n1 > maior: #esse peso e o 2 valor que vai ser comparado com o primeiro peso
            maior = n1 # se o 2 peso for maior que o primeiro MAIOR recebe 2 peso
        if n1 < menor: #se o segundo peso for menor , que o menor q e o primeiro peso
            menor = n1 #menor recebe o primeiro valor
    media = n1 + media
    laco = str(input('Deseja continuar [S|N]: ')).upper().strip()
    if laco != 'S':
        print('Programa finalizado.')
print('-'*100)
print('A média foi de: {:.2f}'.format(media/cont))
print('Maior número foi: {}'.format(maior))
print('Menor número foi: {}'.format(menor))

resp = 'S'
media = maior = menor = soma = c = 0
while resp != 'N':
    numero = int(input('Digite o número: '))
    c += 1
    soma += numero
    media = soma / c
    if c == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < numero:
            menor = numero
    resp = str(input('Deseja continuar [S|N]: ')).upper().strip()

print(f'Você digitou {c} números e a média foi de {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')