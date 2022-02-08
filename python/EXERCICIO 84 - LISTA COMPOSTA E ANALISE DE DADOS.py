dados = list()
pessoas = []
pesados = []
leves = []

maior = menor = 0

while True:
    nome = str(input('Nome: ')).lower()
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    if len(pessoas) == 0:  # se eu nao adicionei nada em pessoas
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

    pessoas.append(dados[:])  # dessa forma cada pessoa vai ficar dentro de uma lista
    dados.clear()  # apagar lista antiga

    resp = ' '
    while resp not in 'S' and resp not in 'N':
        resp = str(input('Deseja continuar[S|N]: ')).upper()
    if resp == 'N':
        break;
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg... ', end='')
for maiores in pessoas:
    if maiores[1] == maior:
        pesados.append(maiores[0])
print(*pesados, sep=',')
print(f'O menor peso foi de {menor}Kg... ', end='')
for menores in pessoas:
    if menores[1] == menor:
        leves.append(menores[0])
print(*leves, sep=', ')