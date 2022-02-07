num = int(input("Escolha um número para a tabuada: "))
for tabuada in range(1,11):  #colocar dentro de tabuada os numeros de 1 a 10
    print('{} X {:2} = {} '.format(num,tabuada,tabuada*num))
    #{:2} para casas decimais