#59 - ler 2 valores e mostrar o menu (1a 5 menu)
#somar,multiplicar, maior, novos numeros (apagar os numeros q tinha)
#e sair do programa.

maior = menor = op = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while op != 5: #flag é o 5 a opção de parada, enquanto não digitar ele o prgrama fica rodando
    print('*' * 40)
    op = int(input('[1] SOMAR\n[2] MULTIPLICAÇÃO\n[3] MAIOR NÚMERO\n[4] VALORES NOVOS\n[5] SAIR\nQual opção deseja: '))
    print('*'*40)
    if op == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}.')
    elif op == 2:
        print(f'A multiplicação entre {n1} X {n2} é {n1*n2}.')
    elif op == 3:
        maior = n1
        menor = n2
        if n1>n2:
            maior = n1
        if n2>n1:
            maior = n2
        if n1 == n2:
            print(f'Números iguais, {n1} e {n2}.')
        print(f'O maior número entre {n1} e {n2} é {maior}.')
    elif op == 4:
        n1 = int(input('Insira o novo valor para o primeiro número: '))
        n2 = int(input('Insira o novo valor para o segundo número: '))
    elif op == 5:
        print('Programa finalizado.')
    else:#caso o numero seja maior q 5
        print('Por favor, informe um número entre 0 e 5 !')
