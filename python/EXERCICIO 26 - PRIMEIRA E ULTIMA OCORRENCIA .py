#faca um programa que leia a letra A e mostre quantas vezes ela aparece e qual a sua posicao
letra = str(input('Digite a palavra: ')).upper().strip()
contA = letra.count('A')
posicao = letra.find('A')
print(f'Tem {contA} letra(s) "A" na palavra.\nSua posição é {posicao+1}')
print('A última posição foi em {} '.format(letra.rfind('A')+1))

#count ele conta
#Se a letra A for a primeira ira aparecer a posicao 0 POR ISSO O +1
#rfind e para ele comecar a procurar a partir da direita que e o fim da frase
#ESPACO CONTA























