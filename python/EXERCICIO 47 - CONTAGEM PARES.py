#MOSTRAR TDS OS NUMEROS PARES QUE ESTAO NO INTERVALO DE 1 A 50
for par in range(1,51):#COLOCOU DE 1 ATE 51 PQ TEM Q MOSTRAR O 50 JA QUE ELE E PAR
    if(par%2==0): #se o resto da divisao for zero entao ele e par
        print(par, end=' ')#esse end deixa o numero do lado " " coloca espaco
print("\n")
#opte por codigos mais simples que nao esforcam tanto o computador
for guanabara in range(0,51,2): #comeca do zero vai ate o 50 de 2 em 2
    print(guanabara, end=' ')