pessoas = []
while True:
    nome = str(input('Nome: ')).upper().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    #0,1,2
    pessoas.append([nome,[n1,n2],media]) #aqui ja fez a lista composta
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar[S|N]: ')).upper().strip()
    if op == 'N':
        break;
print('-='*45)
print(pessoas)
print('-='*45)
print('-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for indice ,alunos in enumerate(pessoas):
    print(f'{indice:<4}{alunos[0]:<10}{alunos[2]:>8}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno: '))
    if opc == 777:
        print('Finalizando.....')
        break;
    if opc<=len(pessoas)-1:
        print(f'Notas de {pessoas[opc][0]} são {pessoas[opc][1]}')
print('<<<< Volte Sempre >>>>')

#refazer