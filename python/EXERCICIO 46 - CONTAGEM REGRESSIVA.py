#indo de 10 ate 0 com uma pausa de 1 segundo
import time
import emoji

#sleep ele faz contagem regressiva
for fogos in range(10,0,-1): #vai ao 10 ao 1, tirando um
    print(fogos)
    time.sleep(1) #nao precisa atribuir a uma variavel, mas colocar dentro do laco
print(emoji.emojize("Fogos estorados !!! :fireworks:",use_aliases=True)) #usar esse use_aliasses pq e necessario para emoji