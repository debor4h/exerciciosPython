#jogar jokenpô, papel,pedra e tesoura
import random #para o pc sortear qual item
from time import sleep #para a palavra ir devagar

escolha = int(input("1 para PEDRA.\n2 para PAPEL.\n3 para TESOURA: "))
print('*'*50)
print("JÔ")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
if escolha == 1:
    print("Você escolheu PEDRA")
elif escolha == 2:
    print("Você escolheu PAPEL")
elif escolha == 3:
    print("Você escolheu TESOURA")
else:
    print("Opção Inválida...")

pc = random.randint(1,3)
if pc == 1:
    print("Sorteado pelo computador PEDRA")
elif pc == 2:
    print("Sorteado pelo computador PAPEL")
else:
    print("Sorteado pelo computador TESOURA")
print('*'*50)

if  escolha == 1 and pc == 1:
    print("Nenhum ganhou porque ambos escolheram PEDRA")
elif escolha == 2 and pc == 2:
    print("Nenhum ganhou porque ambos escolheram PAPEL")
elif escolha == 3 and pc == 3:
    print("Nenhum ganhou porque ambos escolheram TESOURA")

elif pc == 2 and escolha == 1:
    print("Computador ganhou !!!")
elif pc == 2 and escolha == 3:
    print("Você ganhou !!!")

elif pc == 3 and escolha == 1:
    print("Você ganhou !!!")
elif pc == 3 and escolha == 2:
    print("Computador ganhou !!!")

elif pc == 1 and escolha == 2:
    print("Você ganhou !!!")
elif pc == 1 and escolha == 3:
    print("Computador ganhou !!!")


elif escolha == 1 and pc == 2:
    print("Computador ganhou !!!")
elif escolha == 1 and pc == 3:
    print("Você ganhou !!!")

elif escolha == 2 and pc == 1:
    print("Você ganhou !!!")
elif escolha == 2 and pc == 3:
    print("Computador ganhou !!!")

elif escolha == 3 and pc == 1:
    print("Você ganhou !!!")
elif escolha == 3 and pc == 2:
    print("Computador ganhou !!!")
else:
    print("FIM...\nObrigado(a) por jogar !!!")


# outra forma
import random, time  # importando modulo

lista = ['PEDRA', 'PAPEL', 'TESOURA']  # colocando as opcoes dentro da lista
pc = random.choice(lista)  # aqui ele sortea um e coloca dentro de pc

# perguntando ao jogador
jogador = int(input('Suas opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nQual é a sua jogada? '))

# atribuindo os valores
if jogador == 0:  # se jogador jogar 0 , j recebe pedra
    j = 'PEDRA'  # j recebe o nome (string)
elif jogador == 1:
    j = 'PAPEL'
elif jogador == 2:
    j = 'TESOURA'
else:
    print('Opção inválida ! ')  # caso nao seja 0,1,2

# se jogador jogar 0,1,2.Vai dar continuidade ao programa
# aqui é uma condicao aninhado, que so vai mostrar se o acima der true
if jogador == 0 or jogador == 1 or jogador == 2:
    print('JO')
    time.sleep(1)  # forma progreesiva
    print('KEN')
    time.sleep(1)
    print('PO !')

    print('-=' * 25)
    print(f'Computador jogou {pc}')
    print(f'Jogador jogou {j}')
    print('-=' * 25)

    # condicao aninhado
    if j == 'PAPEL' and pc == 'PAPEL':
        print('EMPATE !')
    elif j == 'TESOURA' and pc == 'TESOURA':
        print('EMPATE !')
    elif j == 'PEDRA' and pc == 'PEDRA':
        print('EMPATE !')

    elif j == 'PEDRA' and pc == 'PAPEL':
        print('COMPUTADOR VENCEU !')
    elif j == 'PAPEL' and pc == 'PEDRA':
        print('JOGADOR VENCEU !')

    elif j == 'PEDRA' and pc == 'TESOURA':
        print('JOGADOR VENCEU !')
    elif j == 'TESOURA' and pc == 'PEDRA':
        print('COMPUTADOR VENCEU !')

    elif j == 'PAPEL' and pc == 'TESOURA':
        print('COMPUTADOR VENCEU !')
    elif j == 'TESOURA' and pc == 'PAPEL':
        print('JOGADOR VENCEU !')
    # aqui vai mostrar independente de jogar entre 0-2
else:
    print('Obrigado(a) por jogar !')

# print(pc) #sorteia um
# print(sorted(lista)) # nao precisa colocar o random, faz ficar organizado tanto em alfabetico quanto numerico'
# print(random.shuffle(lista)) #assim nao funciona
# funciona dessa forma
# random.shuffle(lista) #funcao para embaralhar
# print(lista)