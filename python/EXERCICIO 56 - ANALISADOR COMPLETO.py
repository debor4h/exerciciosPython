#treinar
print("---------------------------- SOLUÇÃO GUANABARA -----------------------")
print('-'*70)
print("\n")
somaIdade = 0
mediaIdade = 0
maiorHomem = 0
nomeV = ''
tmulher = 0
for p in range(1,3):
    print('----------- {}ª Pessoa ----------- '.format(p))
    n =str(input("Digite seu nome: ").strip().upper())
    i =int(input("Informe sua idade: "))
    s = str(input("Sexo [M/F]:").strip().upper())
    somaIdade +=i
    if p == 1 and s in 'Mm': #se o sexo for M maiusculo ou m Minisculo
        maiorHomem = i
        nomeV = n
    if s in "Mm" and i>maiorHomem:
        maiorHomem = i
        nomeV = n
    if s in "fF" and i < 20:
        tmulher+=1
mediaIdade = somaIdade/4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O nome do homem mais velho é {} com idade de {}.'.format(nomeV,maiorHomem))
print('São {} com menos de 20 anos.'.format(tmulher))



#nome, idade, sexo de 4 pessoas, mostre a media de idade do grupos
#qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
mulheres=velho=novo=media=0
nomeVelho = nomeNovo= ' '

for dados in range(1,4):
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    media +=idade
    sexo = str(input('Sexo [F|M]: ')).upper().strip()
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        velho = idade
        novo = idade
        nomeNovo = nome
        nomeVelho = nome
    else:
        if idade > velho:
            velho = idade
            nomeVelho = nome
        if idade<novo:
            novo = idade
            nomeNovo = nome

print(f'Há {mulheres} com menos de 20 anos.')
print(f'Há média de idade do grupo é de {media :.2f}')
print(f'Homem mais velho é o {nomeVelho} com idade de {velho}.')
print(f'Homem mais novo é o {nomeNovo} com idade de {novo}.')