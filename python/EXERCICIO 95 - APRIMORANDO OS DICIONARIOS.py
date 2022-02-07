#APRIMORAR O 93 COM MAIS DE UM JOGADOR S OU N
#VAI APARECER UMA TABELA COM COD 0 1 2 NOME  GOLS E A QTD DE GOLS
#LEVANTAMENTO DO JOGADOR TAL
#NO JG 0 FEZ 3 GOLS...
#MOSTRAR MAIS COLOCAR O COD DO JPGADOR SE NAO EXISTIR DAR MSG DE ERRO
#777 PARA PARAR

#SOLUCAO GUANABARA
time = []
partidas = []
jogador = dict()
while True:
    jogador.clear()#limpando pq a cada laco vai ler novos dados
    jogador['nome']=str(input('Digite o nome do jogador: ')).upper()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()  # para nao acumular partidas no looping
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:] #aqui ta fazendo a copia de partidas para dentro do gols
    jogador['total'] = sum(partidas) #sum faz a soma ele conta as partidas
    time.append(jogador.copy())#fazendo a copia
    while True:
        resp = str(input('Quer continuar? [S|N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROU! Responda apenas S ou N')
    if resp == 'N':
        break;
#cabecalho
print('-=' * 30)
print('cod  ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*30)
#tabela
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15} ',end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador, [777] para finalizar: '))
    if busca == 777:
        break
    if busca>=len(time):
        print('Erro, não exite jogador com o código da busca.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i,g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i} fez {g} gols.')
    print('--'*30)
print('<< VOLTE SEMPRE >>')