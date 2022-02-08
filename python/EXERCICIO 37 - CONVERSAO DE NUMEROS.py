num = int(input("Digite um  número inteiro: "))
print('-'*30)
x = int(input("ESCOLHA UMA OPÇÃO:\n[1] para BINARIO.\n[2] para OCTAL.\n[3] para HEXADECIMAL. "))
if x == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num,bin(num)[2:])) #esse bin(num) converte para binario
elif x == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif x==3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num,hex(num)[2:]))
else:
    print("Opção Inválida !!!")

#[2:] fatiamento vai da 2 letra ate o final