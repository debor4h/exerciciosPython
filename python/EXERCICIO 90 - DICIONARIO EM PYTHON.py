#FACA UM PROGRAMA QUE LEIA O NOME E A MEDIA DE UM ALUNO
#E A SITUACAO MAIS DE 7 APROVADO GURDANDO A SITUCAO EM UM DICIONARIO
#NOME E IGUAL A ....
#MEDIA É 3.5
#SITUACAO É == A REPROVADO
#SO P UMA PESSOA

aluno = dict() #criando dicionario
#colocar o nome do dicionario e o seu indice, depois o q ele recebe
aluno['Nome'] = str(input('Qual seu nome: ')).upper().strip()#passando para o maiusculo e tirando os espacos
aluno['Media'] = float(input('Qual a sua média: '))
if 5<= aluno['Media']<7: #se aluno[media] colocar o indice for menor do q 7
    aluno['Situacao'] = 'Recuperação' #recebe reprovado
elif aluno['Media']>=7:#senao
    aluno['Situacao'] = 'Aprovado'#recebe aprovado
else:
    aluno['Situacao'] = 'Aprovado'
print(aluno)
print('-='*30)
#para mostrar tem q colocar o  nome do dicionario e o indice entre aspas ""

#items() é tipo um enumerate
#indice e valor
#para cada indice e valor e aluno
for i,v in aluno.items():
    print(f'{i} é igual a {v}')
#fazer um for ao inves disso
#print(f'Nome é igual a {aluno["nome"]}.')
#print(f'Média é igual a {aluno["media"]}')
#print(f'Situação é igual a {aluno["situacao"]}.')