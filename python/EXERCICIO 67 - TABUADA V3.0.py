while True:
    print('-'*35)
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 35)
    if num < 0: #condicao flag, aqui ele para
        break;
    for tab in range(1,11): #comeca do 1 e vai ate o 10, o 11 nao conta
        print(f'{num:2} X {tab:2} = {num*tab:2}')
        # {:2} para casas decimais
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')