#vogais e consoantes
#tupla com varias palavras
#na palavra aprender temos as vogais a e e
#nao usar acentos
palavras = ('ana','uva','lapis','pedro','estojo',
            'branca','preta','garrafa','suco',
            'carro','casa','cama','cafe')
for p in palavras: #mostrando as palavras
        print()
        print(f' Na palavra {p} temos ',end='')
        for letra in p: #aqui letra sao cada palavras, entao se ana em p
            if letra.lower() in 'aeiou': #se ana tiver as vogais
                print(f'{letra}',end=' ')#printar as vogais

#vogais e consoantes
#tupla com varias palavras
#na palavra aprender temos as vogais a e e
palavras = ('ana','uva','lapis','pedro','estojo','branca','preta','garrafa','suco',
            'carro','casa','cama','cafe','musica','caderno','borracha','caneta','amor',
            'paixao','ilusao','desprezo','humildade','felicidade','sabedoria','conhecimento',
            'persistencia','resiliencia')

for p in palavras:
    print(f'Na palavra {p} temos as vogais ')
    for letra in p:
        if letra.lower() in 'aeiou': #'aeiou' aqui e para informar se e uma delas
            print(letra,end=' ')


#ultimo 76
#uma tupla com varias palavras, nao usar acentos
#DEPOIS MOSTRAR AS VOGAIS
#na palavra aprender temos as vogais a e e
palavras = ('ana','uva','lapis','pedro','estojo','branca','preta','garrafa','suco',
            'carro','casa','cama','cafe','musica','caderno','borracha','caneta','amor',
            'paixao','ilusao','desprezo','humildade','felicidade','sabedoria','conhecimento',
            'persistencia','resiliencia')
for p in palavras:#para p em palavras
    print(f'\nNa palavra {p} temos ',end='')#\n para as letras ficarem do lado direito
    for letra in p:#para letra em p
        #colocou no minusculo pq escreveu as palavras em minusculos
        #se em letra tem aeiou faca
        if letra.lower() in 'aeiou': #'aeiou' aqui e para informar se e uma delas
            print(letra,end=' ')
