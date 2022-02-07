a = input('Digite algo: ')
#a é um objeto
#isupper() .. é metodo
print('Seu tipo primitivo é: {}'.format(type(a))) #mostrando seu tipo
print('Somente númerico: {}'.format(a.isnumeric())) #é numero se sim da True
print('Somente alfabético {}'.format(a.isalpha())) #é letra se sim da True
print('Somente em maiúsculo: {}'.format(a.isupper()))#para ver se tds estao em maiusculas se sim da True
print('Somente alfanúmerico {}'.format(a.isalnum())) #letras e numeros se sim da True
print('Somente espaços: {}'.format(a.isspace())) #para saber se a palavra tem espaços
print('Somente em minúscula: {}'.format(a.islower()))#para saber se a palavra está em minúsculo
print('Está capitalizada: {}'.format(a.istitle))#para saber se está capitalizada, primeira letra em maiúscula