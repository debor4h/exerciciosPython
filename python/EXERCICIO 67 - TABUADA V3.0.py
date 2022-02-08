while True:
    print('-'*35)
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 35)
    if num < 0:
        break;
    for tab in range(1,11):
        print(f'{num:2} X {tab:2} = {num*tab:2}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')