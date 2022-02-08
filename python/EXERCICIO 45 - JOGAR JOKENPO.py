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
