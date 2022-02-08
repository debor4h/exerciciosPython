#FACA UM PROGRAMA QUE INFORME O PRIMEIRO E ULTIMO NOME
nome = str(input('Digite seu nome: ')).upper().strip()
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu último nome é {nome.split()[-1]}')


