#str e string, split tira os espacos dela na hora da digitacao do usuario do final e do inicio menos o do meio
frase = str(input('Digite uma frase: ')).strip().upper() #tira os espacos e passa para o maiusculo
inverso = ''
palavras = frase.split()
#join juntas
junto = ''.join(palavras)
#o primeiro -1 e a ultima posicao, o segundo -1 e pq a primeira letra é 0 e ele tem q pegar
#esse o entao ele vai ate -1 pq antes do 0 ja e negativo, e por ser de tras p frente ele vai de -1 que e o terceiro -1
for letras in range(len(frase)-1,-1,-1):
   #print(junto[letras]) ele mostra de tras para frente
    inverso += junto[letras]
print(junto, inverso) #ele de tras pra frente e de frente tem q ser a mesma coisa
if inverso == junto:
    print("É palíndromo!")
else:
    print("Não é palíndromo!")

#palindroma e uma palavra que de tras para a frente e vice e versa e a msm coisa

print('-'*70)
a = str(input("Digite uma frase: ")).upper() .replace("","") #coloca para o maiusculo e tira os espacos
#a[::-1] aqui é a palavra de tras p frente
if a == a[::-1]: #aqui o primeiro : representa o comeca da frase, o segundo : representa o fim e o -1 ou numeros negativos fala que comeca da direita p esquerda
    print("A frase é palíndromo")
else:
    print("A frase não é um palíndromo")