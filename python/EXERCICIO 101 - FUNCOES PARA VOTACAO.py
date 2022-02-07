def voto(ano_nascimento): #criacao da funcao
    #colocado dentro de voto o ano para economizar memoria, e so funciona aqui dentro
    from datetime import date  # importacao para pegar o ano atual
    anoAtual = date.today().year  # ano atual
    idade = abs(ano_nascimento - anoAtual)

    if idade >= 18 and idade < 64:
        return f'Com {idade} anos: VOTO OBRIGÁTORIO.'
    elif idade <= 15:
        return f'Com {idade} anos: NÃO VOTA.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


#programa principal
print('-'*30)
ano = int(input('Em que nao você nasceu: '))
print(voto(ano))#esse ano ele vai jogar dentro de ano nascimento que e aonde esta
# td o processo do programa