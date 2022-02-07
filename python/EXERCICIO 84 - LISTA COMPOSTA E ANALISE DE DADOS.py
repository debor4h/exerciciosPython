pessoas = [[],[]]
maior = menor = cont= 0
while True:
    nome = str(input('Nome: ')).upper().strip()
    peso = float(input('Peso: '))
    pessoas[0].append(peso)
    pessoas[1].append(nome)
    for i in enumerate(pessoas[0]):
      print(i[1])
      if i[0] == 0:
          maior = i[1]
          menor = i[1]
      else:
          if i[1]>maior:
              maior = i[1]
          if i[1]<menor:
              menor = i[1]
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar[S|N]: ')).upper()
    if op == 'N':
        break;

print(f'A quantidade de pessoas cadastradas foram: {len(pessoas)+1}')
print(f'Maior peso foi de {maior}, por: ',end=' ')
for i,v in enumerate(pessoas):
    if v==maior:
        for i,v in enumerate(pessoas[1]):
            print(f'{v}',end=' ')
print()
print(f'Menor peso foi de {menor}, por: ',end=' ')


print('-='*80)

t = []
p = []
ma=me=0
while True:
    t.append(str(input('Nome: ')))
    t.append(float(input('Peso: ')))
    if len(p) == 0: #se nao cadastrou ninguem ainda
        ma = me = t[1] #t[1] e o peso
    else:
        if t[1]>ma:
            ma=t[1]
        if t[1]<me:
            me=t[1]
    p.append(t[:])#adicionando ao t
    t.clear()
    resp = str(input('Deseja continuar[S/N]: '))
    if resp in 'Nn':
        break;

print(f'Os dados foram: {p}')
print(f'Ao todo, você cadastrou {len(p)} pessoas.')
print(f'O maior peso foi de {ma} KG ',end='')
for pp in p:
    if pp[1]==ma:
        print(f'{pp[0]}...',end='')
print()
print(f'O menor peso foi de {me} KG ',end='')
for pp in p :
    if pp[1]==me:
        print(f'{pp[0]}....',end='')



numeros = [[],[]]


for total in range(1,8):
  num = int(input('Digite os números: '))
  numeros.append(num)
  if num%2==0:
    numeros[0].append(num)
  else:
    numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print('*'*25)

print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')

print()
#outro exemplo

numeros = [[],[]]


for total in range(1,8):
  num = int(input('Digite os números: '))
  numeros.append(num)
  if num%2==0:
    numeros[0].append(num)
  else:
    numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print('*'*25)

print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')


#solucao guanabara

temp = list()
princ = list()
maio=menor=0

while True:
  temp.append(str(input('Nome: ')).upper())
  temp.append(float(input('Peso: ')))
  if len(princ) == 0: #se eu nao coloquei ninguem ainda
    maior=menor=temp[1] #temp[1] e o peso
    # é o msm que isso
    # maior = temp[1]
    # menor = temp[1]
  else:
    if temp[1]>maior:
      maior = temp[1]
    if temp[1]<menor:
      menor = temp[1]
  #aqui esta fazendo copia, se mudar um o outro nao muda
  #sem a copia os nomes e pesos de cada pessoa fica em uma lista  so
  #com a copia cada nome fica em uma lista dentro de uma lista
  princ.append(temp[:])
  temp.clear()
  op = ' '
  while op not in 'S' and op not in 'N':
    op = str(input('Quer continuar[S|N]: ')).upper()
  if op == 'N':
    break;
print('-='*15)
print(f'Os dados foram {princ}')
print(f'Ao todo foram cadastrados {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg...',end = ' ')
for p in princ:
  if p[1] == maior:
    print(f'{p[0]}',end = ' ')
print(f'O menor peso foi de {menor}Kg...',end = '')
print()
for p in princ:
  if p[1] == menor:
    print(f'{p[0]}',end = '')

dados = list()
pessoas = []
pesados = []
leves = []

maior = menor = 0

while True:
    nome = str(input('Nome: ')).lower()
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    if len(pessoas) == 0:  # se eu nao adicionei nada em pessoas
        # if dados[1] == peso: vai dar errado pq ele abaixo apaga td de dado
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

    pessoas.append(dados[:])  # dessa forma cada pessoa vai ficar dentro de uma lista
    dados.clear()  # apagar lista antiga

    resp = ' '
    while resp not in 'S' and resp not in 'N':
        resp = str(input('Deseja continuar[S|N]: ')).upper()
    if resp == 'N':
        break;
print(f'Foram cadastradas {len(pessoas)} pessoas.')
# print(pessoas)
print(f'O maior peso foi de {maior}Kg... ', end='')
# para cada "pessoa" em pessoa colocar dentro de maiores
for maiores in pessoas:
    if maiores[1] == maior:  # se maiores 1 que e peso for igual a maior
        pesados.append(maiores[0])  # adc dentro da lista maiores
print(*pesados, sep=',')  # para nao mostrar os [] colocar * e o sep é o separador
print(f'O menor peso foi de {menor}Kg... ', end='')
for menores in pessoas:
    if menores[1] == menor:
        leves.append(menores[0])
print(*leves, sep=', ')