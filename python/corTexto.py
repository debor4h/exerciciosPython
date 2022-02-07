#codigo ansi
#style e estilo do texto
#text e cor do texto
#back e cor de fundo do texto
#ex \033[0;33;44m CODIGO DE COR
#nao precisa colocar as tres opcoes
#0;33;44 isso sao as definicoes

print('\033[31;43mOlá mundo!!!') #letra red, fundo amarelo
print('\033[7;30mOlá mundo!!!\033[m')#formatacao final para ir so ate a letra

a =3
b =5
print('Os valores sao \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Bieber'
print('Prazer {}{}{}'.format('\033[4;34m',nome,'\033[m'))

#outra forma
n = 'Justin'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m' }

print('FORMATAÇÃO: {}{}{} '.format(cores['pretoebranco'],n,cores['limpa']))