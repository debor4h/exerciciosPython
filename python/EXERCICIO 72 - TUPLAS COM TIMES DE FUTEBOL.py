#tupla com os times de futebool
#5 primeiros colocados
#os 4 ultimos colocados na tabela
#lista com os times em ordem alfabetica
#em que posicao esta chapecoense

times = ('Atletico-MG','Palmeiras','Fortaleza','Bragantino','Flamengo','Corinthians','Atletico-GO',
         'Ceara-SC','Atletico-PR','Internacional','Santos','Sao Paulo','Juventude','Cuiaba','Bahia',
         'Fluminense','Gremio','Sport Recife','America-MG','Chapecoense')

print('=-'*50)
print(f'Os cinco primeiros times são: {times[:5]}')
print('=-'*50)
print(f'Os quatro últimos times são: {times[16:]}')
print('=-'*50)
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print('=-'*50)
for i,v in enumerate(times):
    if v == 'Chapecoense':
        print(f'Chapeconse está na posição: {i+1} º')

print('=-'*50)

#73
times = ('Palmeiras','Atlético-MG','Fortaleza','Bragantino','Atlético-PR','Flamengo','Ceára SC',
         'Bahia','Fluminense','Santos','Atlético-GO','Corinthians','Internacional','Juventude',
         'Cuibá','São Paulo','Sport-Recife','América-MG','Grêmio','Chapecoense')

print('=-'*145)
print(f'Os times do Brasileirão: {times}')
print('=-'*145)

#os primeiros 5 colocados
#print('Os cinco primeiros colocados são: {times[0:5]} ')fatiamento ignora o ultimo
print('Os cinco primeiros colocados são: ',end = ' ')
for cinco in range(0,5):
    print(f'{times[cinco]},',end = ' ')
print('\n')
print('=-'*145)
#os ultimos 5 colocados
print(f'Os últimos 4 colocados são: ',end = ' ') #mostra o ultimo colocado
for ultimo in range (16,len(times)):
    print(f'{times[ultimo]}',end = ' ') #mostra o ultimo colocado
print('\n')
print('=-'*145)
#times em ordem alfabetica de A ate Z
print(f'Em ordem alfabetica: {sorted(times)}')
#em q posicao o chapecoense esta, numero e nome
print(f'Chapecoense está na posição {times.index("Chapecoense")+1}ª posição.')


