num = int(input("Escolha um número para a tabuada: "))
for tabuada in range(1,11):
    print('{} X {:2} = {} '.format(num,tabuada,tabuada*num))
