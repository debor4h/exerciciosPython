#LER NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO,
#CADASTRAR C IDADE
#EM UM DICIONARIO SE CTPS(SE TIVER CARTEIRA DE TRABALHO)
#FOR DIFERENTE OU SEJA SE TRABALHA DE ZERO O DICIONARIO RECEBERAO ANO
#DE CONTRATACAO E O SALARIO E COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR
from datetime import date
ano = date.today().year
trabalhador = dict() #dicionario variavel
trabalhador['nome']=str(input('Nome: ')).upper()
nascimento =int(input('Qual ano nasceu: '))
trabalhador['idade'] =ano-nascimento
trabalhador['ctps']=int(input('Carteira de trabalho [Não tem - 0]: '))
if trabalhador['ctps'] !=0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    x = 32  - (ano - trabalhador['contratacao'])
    trabalhador['aposentadoria'] = (ano + x)-nascimento
print('-=' * 40)
print(trabalhador)
print('-='*40)
for i,v in trabalhador.items():
    print(f'-- {i} tem o valor {v}')