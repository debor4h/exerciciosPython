#64 - tratando varios valores,777 para parar flag, mostrar a
#soma e quantos nuemeros foram digitados exceto o flag

soma = quant = numero = 0
while numero !=777: #enquanto op nao for 777 que é o flag para parar o programa
    numero = int(input('Digite um número [777 para parar]: '))
    if numero!=777:
      soma += numero #soma
      quant += 1 #quantidade
    elif numero == 777:
      print(f'A soma deu {soma}.')
print(f'A quantidade de números digitados foi {quant}.')
