#nao entendi muito
frase = str(input('Digite uma frase: ')).strip().upper() #tira os espacos e passa para o maiusculo
inverso = ''
palavras = frase.split()
junto = ''.join(palavras)
for letras in range(len(frase)-1,-1,-1):
    inverso += junto[letras]
print(junto, inverso) #ele de tras pra frente e de frente tem q ser a mesma coisa
if inverso == junto:
    print("É palíndromo!")
else:
    print("Não é palíndromo!")

#palindroma e uma palavra que de tras para a frente e vice e versa tem o mesmo resultado

print('-'*70)
a = str(input("Digite uma frase: ")).upper() .replace("","") #coloca para o maiusculo e tira os espacos
#a[::-1] aqui é a palavra de tras p frente
if a == a[::-1]: #aqui o primeiro : representa o comeca da frase, o segundo : representa o fim e o -1 ou numeros negativos fala que comeca da direita p esquerda
    print("A frase é palíndromo")
else:
    print("A frase não é um palíndromo")