#LEIA UM NUMERO E MOSTRE A SEQUENCIA DE FIBONACCI, VAI MOSTRA OS NUMERO PEDIDO
#EX DIGITA 7 ELE VAI MOSTRAR OS 7 PRIMEIROS TERMOS DESSA SEQUENCIA

#comeca com 1,1 depois e a soma desse numero
#ex 2, 2 mais 1 e 3
#1,1,2,3, 3 + 2 e 5
#1,1,2,3,5......

#NAO CONSEGUIR RESOLVER, SOLUCAO GUANABARA



numero = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
contador = 3  # pq ja mostrou os 2 primeiros termos
while contador <= numero:
        t3 = t1 + t2
        print(f'-> {t3}', end='')
        t1 = t2
        t2 = t3
        contador += 1
print('-> FIM')