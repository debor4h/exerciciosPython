#59 - ler 2 valores e mostrar o menu (1a 5 menu)
#somar,multiplicar, maior, novos numeros (apagar os numeros q tinha)
#e sair do programa.
maior = menor = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

op = 0
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

menu = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while menu != 5:
    op = int(input('1 - somar\n2 - multiplicar\n3 - maior\n4 - novos números\n5 - sair do programa\n '))
    if op == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} resultou em {}.'.format(n1,n2,soma))
    elif op == 2:
        mult = n1*n2
        print('A multiplicação entre os números {} e {} resultou em {}.'.format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é {}.'.format(n1,n2,maior))
        elif n1 < n2:
            maior = n2
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
        else:
            print('Ambos números são iguais, {} e {}.'.format(n1,n2))
    elif op == 4:
        novoN1 = int(input('Digite um novo valor para n1: '))
        n1 = novoN1
        novoN2 = int(input('Digite um novo valor para n2: '))
        n2 = novoN2
        print('Os novos valores são {} e {}.'.format(n1,n2))
    else:
        print('Obrigado por jogar !!!')
    menu = int(input('Deseja continuar [5 - Não e 1 - SIM]: '))
    if menu == 5:
        print('Obrigado por jogar !!!')
