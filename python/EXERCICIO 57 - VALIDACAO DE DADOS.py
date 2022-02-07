sexo = ' '
while sexo != 'M' and sexo !=  'F':
    sexo = str(input('Digite seu sexo [F|M]: ')).upper()
    if sexo == 'F':
        print('Feminino')
    elif sexo == 'M':
        print('Masculino')
    else:
        print('Sexo inválido, apenas digite F para FEMININO ou M para MASCULINO.')


#PROGRAMA QUE SO ACEITA F e M. E NAO PARE ATE CONSEGUIR
teste = 'S'
while teste == 'S':
    sexo = str(input('Digite seu sexo [F|M]: ')).upper()
    if sexo == 'F' or sexo == 'M':
        if sexo == 'F':
            print('\033[35mSeu sexo é {} [FEMININO].\033[m'.format(sexo))
        elif sexo == 'M':
            print('\033[35mSeu sexo é {} [MASCULINO].\033[m'.format(sexo))
        print('Sexo registrado com sucesso!!!')
        teste = str(input('Deseja cadastrar mais sexo [S|N]: ')).upper()
    elif sexo != 'F' or sexo != 'M':
        teste = str(input('Opção inválida, deseja tentar novamente [S|N]: ')).upper()
print('\033[31mVocê finalizou o programa, obrigado. !!!\033[m')