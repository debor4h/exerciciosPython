from datetime import date #importando ano
ano = date.today().year
maioridade = menorIdade = 0

for pessoas in range(1,8):
    anoNascimento = int(input(f'Em que ano a {pessoas}º nasceu? '))
    if (ano - anoNascimento) >= 21:
        maioridade=maioridade+1
    elif (ano - anoNascimento) < 21:
        menorIdade = menorIdade+1

print(f'Há {maioridade} pessoas maiores de idade.')
print(f'Há {menorIdade} pessoas menores de idade.')
