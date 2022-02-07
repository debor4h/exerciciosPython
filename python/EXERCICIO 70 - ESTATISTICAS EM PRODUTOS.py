print('-'*30)
x = 'LOJA SUPER BARATÃO'
print(f'{ x :^30}')
print('-'*30)
tot = mil = barato = cont = maior = menor = 0
nomebarato = ' '
while True:
    produto = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço: R$'))
    cont +=1
    if cont == 1: #o priemeiro valor
        maior = preco#fica com o maior
        menor = preco#fica com o menor
    else:#aqui ele ja comeca a comparar com os outros valores
        if preco>maior:#se segundo valor for maior que o primeiro ele vai  pegar o valor do primeiro
            maior = preco
        if preco<menor:
            menor = preco
            nomebarato = produto
    tot += preco
    if preco > 1000:
        mil+=1
    op = ' '
    while op not in 'SN': #enquanto op  nao estiver dentro de s ou n
        op = str(input('Quer continuar[S|N]: ')).upper().strip()
    if op == 'N':
        break;
print('--------------- FIM DO PROGRAMA ---------------')
print(f'O total da compra foi de R${tot :.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custou R${menor :.2f}')