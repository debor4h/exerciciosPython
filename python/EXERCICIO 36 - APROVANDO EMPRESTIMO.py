valor = float(input('Informe o valor da casa: '))
print('-'*40);#aqui vai formar 40 linhas tracadas
salario = float(input('Informe o seu salário: '))
print('-'*40);
anos = int(input('Em quantos anos a casa será paga: '))
print('-'*40);
sal = ((salario*30)/100);
prestacao = valor / (anos*12);
if prestacao > sal:
    print("Empréstimo Negado !!!")
else: #:.2f para limitar 2 casas decimais . \n ele vai escrever na linha de baixo
    print("A casa será paga em {:.2f} prestações.\nEmpréstimo concedido com sucesso !!!".format(prestacao))

