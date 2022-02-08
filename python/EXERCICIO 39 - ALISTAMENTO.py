from datetime import date

anoAtual = date.today().year #date.today().year - funcao do pc para saber o ano atual
ano = int(input("Ano de nascimento: "))
sexo = str(input("Qual seu sexo F ou M: ")).upper().strip()
idade = anoAtual - ano;

if sexo == 'M' and idade == 18:
    print('Chegou a hora de se alistar! ')
elif sexo == 'M' and idade > 18:
    print(f'Já passou {idade - 18} de se alistar..')
elif sexo == 'M' and idade < 18:
    print(f'Ainda não deu a hora.  Falta {18 - idade} anos para ser alistar..')
else:
    print('Não precisa se alistar pois você é mulher !')