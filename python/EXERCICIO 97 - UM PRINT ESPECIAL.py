def escreva(texto):
    linha = 0
    print(texto)
    while linha<len(texto):
        print('~',end='')
        linha+=1
    print()

escreva('Gustavo Guanabara')
escreva('Curso Em Pyhton')
escreva('CeV')
escreva('   Olá, mundo!')

print('*'*50)

#solucao guanabara
def esq(mens):
    tamanho = len(mens) + 4 # +4 pq tem 2 nas baradas de cada lado
    print('~' * tamanho)
    print(mens)
    print('~' * tamanho)


esq('Gustavo Guanabara')
esq('Curso Em Pyhton')
esq('CeV')