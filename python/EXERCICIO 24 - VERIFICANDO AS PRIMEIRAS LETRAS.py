#crie um programa que informe se comeca ou nao uma palavra com SANTO true ou falso
p=str(input('Digite o nome da cidade: ')).title().strip()#STRIP TIRA O ESPACO, TITLE USAR SO EM STRING E CAPITALIZE A LETRA
a =p.split()#ELE NAO CONTA OS ESPACOS DE UMA PALAVRA PARA OUTRA ASSIM ELE COMECA A CONTA DENOVO
print('Começa com Santo? {}'.format('Santo' in a[0]))
#necessario usar o strip para tirar os espacos iniciais e finais
#upper vai colocar tds as palavras para maiusculo caso ele escreva SaNtOs
#slipt na posicao 0 e a primeira posicao


cidade = str(input('Qual cidade você nasceu? ')).upper().strip()#passando para o maiusculo e tirando os espacos
resultado = cidade.split()[0] == 'SANTO' #dividindo em blocos a cada espaco e pegando o indice 0 que e o primeiro e vendo se tal e == a SANTO
print(f'A sua cidade começa com SANTO? {resultado}, chama-se {cidade}.')