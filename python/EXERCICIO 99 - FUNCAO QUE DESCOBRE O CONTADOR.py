#chamar 5 valores
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#analisando os valores passados..
#1 2 3 Foram informados 3 valores ao todos.
#o maior valor informado foi 3.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#se for zero o maior valor vai ser zero
def valores(*n):
    maior = menor = 0
    print('-'*35)
    print('Analisando os valores passados...')
    print(*n,sep=' ',end=' ')
    tamanho = len(n)
    print(f'Foram informados {tamanho} valores ao todos.')
    #print(f'O maior valor informado foi {max(n)}')
    for tp in n:
        if tp == 1:
            maior = tp
            menor = tp
        else:
            if tp>maior:
                maior = tp
            if tp<menor:
                menor = tp
    print(f'O maior valor informado foi {maior}')


valores(1,2,3,4,5)
valores(12,34,5)
valores(78,6,45,32)
valores(7)
valores(20,21,22,23)
valores()
valores(0)