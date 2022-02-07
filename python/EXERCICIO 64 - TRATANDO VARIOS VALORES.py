#64 - tratando varios valores,777 para parar flag, mostrar a
#soma e quantos nuemeros foram digitados exceto o flag

soma = quant = numero = 0
while numero !=777: #enquanto op nao or 777 que e o flag, para parar o programa
    numero = int(input('Digite um número [777 para parar]: '))
    if numero!=777:
      soma += numero #soma
      quant += 1 #quantidade
    elif numero == 777:
      print(f'A soma deu {soma}.')
print(f'A quantidade de números digitados foi {quant}.')

laco = 0 #laco
cont = 0 #contador
soma = 0 #soma
while laco != 777: #enquanto laco for diferente de 777
   laco = int(input('Digite um número [777 para parar]: ')) #ira aparecer isso
   if laco !=777: #desconsiderando o flag, #se laco for diferente de 777
       cont += 1 #conta +1
       soma = soma + laco #soma e == ao laco + soma que atribuira na variavel soma
   print('Numero: {}'.format(laco))
print('Foram digitados {} números.'.format(cont))
print('A soma entre eles resultou em: {}'.format(soma))