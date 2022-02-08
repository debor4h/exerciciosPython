#r e razao de quantos em quantos vai pular
#pa e a subtracao da razao com o seu anterior, ex razao é 2 ,
a1= int(input('Indique o primeiro termo da PA: '))
r = int(input('Indique a razão da PA: '))
an = a1 + (10-1)*r #esse -1 é da formula
#an = 2+9*2=20
while a1 <= an:
    print(a1, end=' ')
    a1 += r
print('FIM')


#progressao aritmetica mostrar os 10 primeiros termos
#an=a1 + r·(n-1)  FORMULA

#N→ é a posição do termo;

#a1→ é o primeiro termo;

#r → razão.

#nao entendi muito