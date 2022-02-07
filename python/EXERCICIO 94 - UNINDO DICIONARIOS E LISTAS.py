#NOME IDADE E SEXO DE MUITAS PESSOAS S OU N
#SOMAR AS IDADE E CALCULAR A MEDIA DO GRUPO
#MOSTRAR OS NOMES DA MULHERES CADASTRADAS
#QUANTAS PESSOAS FORAM CADASTRADAS
#LISTA DE PESSOAS QUE ESTAO ACIMA DA MEDIA (IDADE)
#GUARDE OS DADOS EM UM DICIONARIO DE CADA PESSOA E TDS DIC EM UMA LISTA

pessoas =dict() #criando dicionario
soma =  0
mulheres = []
acima = list()
todos = list()
while True:
    pessoas['nome']=str(input('Nome: ')).upper().strip()
    while True:
        pessoas['sexo']=str(input('Sexo [M|F]: ')).upper().strip()
        if pessoas['sexo'] in 'MF':
            break;
        print('Erro digite apenas F ou M...')
        if pessoas['sexo'] == 'F':
            mulheres.append(pessoas['nome'])
    pessoas['idade']=int(input('Idade: '))
    todos.append(pessoas)
    soma += pessoas['idade']
    media = soma/len(pessoas)
    if media < pessoas['idade']:
        acima.append(pessoas['nome'])
        acima.append(pessoas['sexo'])
        acima.append(pessoas['idade'])
    op =' '
    while op not in 'SN':
        op = str(input('Deseja continuar[S|N]: ')).upper().strip()
        if op not in 'SN':
            print('Responda apenas com S ou N...')
    if op == 'N':
        break;

print('-='*45)
print(f'A) Ao todo foram {len(todos)} pessoas cadastradas.')
print(f'B) A média de idade é de {media :.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end =' ')
print(*mulheres,sep=',')
print(f'D) Lista das pessoas que estão acima da média ')
for v in acima:
    print(f'{v}',end = ' ')
    print()
