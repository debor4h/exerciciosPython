tot = 0
primo = int(input("Digite um número: ")) #perguntar numero inteiro
for i in range(1,primo+1): #PRIMO MAIS UM PQ O PRIMO TEM Q APARECER
    if primo%i==0: #se numero for divisivel por tds os numeros de antes dele
        print('\033[34m',end=' ')#codigo de cores. SE FOR DIVISIVEL ELE VAI PINTAR O NUMERO
        tot +=1
    else:#END DEIXA DO LADO ' ' E ESSE ESPACO NO MEIO E PARA DAR ESPACO
        print('\033[m',end=' ')#SE NAO FOR DIVISIVEL ELE NAO VAI PINTAR O NUMERO
    print('{}'.format(i),end=' ')
print('\nO número {} foi divisível {} vezes.'.format(primo,tot))
#se for divisivel por 2 numeros é primo
if tot == 2:
    print("É primo.")
else:
    print("Não é primo.")

print('-'*100)
#outro jeito para saber se é primo

a = int(input("Digite outro número para o exemplo: "))
contador = 0 #vai conta os numeros primos

for cont in range(1,a+1):
    if a%cont == 0:
        contador+=1
print("O número {} foi divisível {} vezes !".format(a,contador))

if contador == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")