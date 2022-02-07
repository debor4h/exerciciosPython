def fatorial (num):
    print('------------------------------------------------')
    print(num)
    for numero in range(num,0,-1):
        print(numero)

num = int(input('Digite um número para calcular o fatorial: '))
print(fatorial(num), end = " ") #coloca dessa forma para mostrar