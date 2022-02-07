from datetime import date #importando ano
ano = date.today().year
maioridade = menorIdade = 0

for pessoas in range(1,8): # para cada pessoa faca 7 vezes, ele nao conta o ultimo
    anoNascimento = int(input(f'Em que ano a {pessoas}º nasceu? '))
    if (ano - anoNascimento) >= 21:
        maioridade=maioridade+1
    elif (ano - anoNascimento) < 21:
        menorIdade = menorIdade+1

print(f'Há {maioridade} pessoas maiores de idade.')
print(f'Há {menorIdade} pessoas menores de idade.')


from datetime import date #importacao da data
data = date.today().year # aqui ele pega o ano atual

#sao os acumuladores
totMaior = 0
totMenor = 0

for anos in range (1,8):
    ano = int(input("Digite o seu ano de nascimento, {}ª pessoa: ".format(anos)))
    diferenca = data - ano
    if diferenca >= 21:
      totMaior +=1
    else:
       totMenor+=1

print('-'*70)

print("Ao todo {} maiores de idade.".format(totMaior))
print("Ao todo {} menores de idade.".format(totMenor))