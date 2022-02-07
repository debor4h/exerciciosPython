salario = float(input('Informe o seu salário: R$ '))
if salario >1250.00:
    print('Aumento de 10%:',(salario*0.10)+salario)
elif salario <= 1250.00:
    print('Aumento de 15%:',(salario*0.15)+salario)

