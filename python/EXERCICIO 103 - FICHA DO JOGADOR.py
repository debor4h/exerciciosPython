def ficha(jogador , gols):
    if len(jogador) == 0 :
        jogador = '<desconhecido>'
    elif type(gols) == str :
        gols = 0
    return f'Jogador(a) {jogador} fez {gols} gol(s) no campeonato.'


#programa principal
nome = str(input('Nome do jogador: ')).title().strip()
gol = str(input('Gols: '))
print(ficha(nome,gol))