#Diga se a pessoa tem silva no nome
sobrenome = str(input('Qual seu nome e sobrenome: ')).upper().strip()
if sobrenome == 'SILVA' and len(sobrenome) == 5:
    print('Tem SILVA no sobrenome')
else:
    print('Não tem SILVA no sobrenome')
