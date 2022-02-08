tot = 0
primo = int(input("Digite um número: "))
for i in range(1,primo+1):
    if primo%i==0: #se numero for divisivel por tds os numeros de antes dele
        print('\033[34m',end=' ')#codigo de cores.SE FOR DIVISIVEL ELE VAI PINTAR O NUMERO
        tot +=1
    else:
        print('\033[m',end=' ')
    print('{}'.format(i),end=' ')
print('\nO número {} foi divisível {} vezes.'.format(primo,tot))
if tot == 2:
    print("É primo.")
else:
    print("Não é primo.")

print('-'*100)
