#faca um programa que leia a letra A e mostre quantas vezes ela aparece e qual a sua posicao
#1 e ultima vez
frase = str(input('Digite uma frase: ')).strip().upper()
apa = frase.count('A') #COUNT ELE CONTA AS PALAVRAS DE A
print('A palavra A, aparece {} '.format(apa))
#Se a letra A for a primeira ira aparecer a posicao 0 POR ISSO O +1
print('A primeira posição foi em {} '.format(frase.find('A')+1))
print('A última posição foi em {} '.format(frase.rfind('A')+1))
#rfind e para ele comecar a procurar a partir da direita que e o fim da frase
#ESPACO CONTA
















