#ultimo 76
#uma tupla com varias palavras, nao usar acentos
#DEPOIS MOSTRAR AS VOGAIS
#na palavra aprender temos as vogais a e e
palavras = ('ana','uva','lapis','pedro','estojo','branca','preta','garrafa','suco',
            'carro','casa','cama','cafe','musica','caderno','borracha','caneta','amor',
            'paixao','ilusao','desprezo','humildade','felicidade','sabedoria','conhecimento',
            'persistencia','resiliencia')
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou': #'aeiou' aqui e para informar se e uma delas
            print(letra,end=' ')
