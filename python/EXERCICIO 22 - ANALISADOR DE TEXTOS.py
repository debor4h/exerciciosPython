#crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com tds as letras maiusculas
#Com todas as letras minusculas
#Quantas letras ao tdo sem os espacos
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip() #para nao contar os espacos
print(nome.upper())#colocar para o maiusculo
print(nome.lower())#colocar para o minusculo
print(len(nome)-nome.count(' ')) #para nao contar os espacos
#print(nome.find(' ')) #outra forma de tirar os espacos
print(len(nome.replace(" ","")))#trocar espaco vazio por nada vazio
print(len(nome.split()[0]))#aparece a quantidade de letras da primeira posicao
#pq no split ele para de contar quando acha espaço, e o a divisao e do 0,1,2 ...