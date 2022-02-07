#refazer o 35
a = float(input("Informe o 1º segmento: "))
b = float(input("Informe o 2º segmento: "))
c = float(input("Informe o 3º segmento: "))

if a+b>c and b+c>a and c+a>b:
    print('Os segmentos acima podem formar um triângulo.')
    if a==b and b==c:
        print('Triângulo Equilátero.')
    elif a!=b and b!=c and c!=a :  #!= é diferente
        print('Triângulo Escaleno.')
    #elif a==b and b!=c:
    else: #aqui colocar esse else por causa do if
        print('Triângulo Isósceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')