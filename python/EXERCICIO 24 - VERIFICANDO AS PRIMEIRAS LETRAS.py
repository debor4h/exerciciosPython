#crie um programa que informe se comeca ou nao uma palavra com SANTO true ou falso

cidade = str(input('Qual cidade você nasceu? ')).upper().strip()#passando para o maiusculo e tirando os espacos
resultado = cidade.split()[0] == 'SANTO' #dividindo em blocos a cada espaco e pegando o indice 0 que e o primeiro e vendo se tal e == a SANTO
print(f'A sua cidade começa com SANTO? {resultado}, chama-se {cidade}.')