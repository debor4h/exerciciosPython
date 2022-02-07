#NOME DO JAGADOR E QUANTAS PARTIDAS ELE
#JOGOU E A QTD DE GOLS FEITO EM CAD PARTIDA,
#SERA GUARDADO EM UM DICIONARIO
#EX 5 PARTIDAS
#QUANT GOLS NA PARTIDA 0 NA
#(1...)
#MOSTRAR O DICIONARIO
#MOSTRAR OS VALUES DE CADA CAMPO
#LACO NA PARTIDA 0, FEZ 2 GOLS.
#FOI UM TOTAL DE 9 GOLS
jogador = dict() #declarando dicionario
lista = list() #declarando lista
jg = 0
jogador['nome']=str(input('Qual é seu nome: ')).upper().strip()
jogador['partidas']=int(input('Quantas partidas jogou? '))

for laco in range(1,(jogador['partidas']+1)):
    jg += int(input(f'Quantos gols fez na {laco} partida: '))
    lista.append(jg)
    jogador['gols'] = lista
    jogador['total']=jg
print('-='*50)
print(jogador)
print('-='*50)
for i,v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print('-='*50)
print(f'Jogador(a) {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f' => Na partida {i},fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')