maiores = homens = mulheres = 0
while True:
    print('-'*30)
    print('CADASTRO DE PESSOA')
    print('-' * 30)
    idade = int(input('Qual sua idade: '))
    sexo = ' ' #iniciando a variavel pq e string entao tem q iniciar entre ' '
    while sexo not in 'FM':#enquanto sexo nao e f ou m, repete esse laco
        sexo = str(input('Qual seu sexo [F|M]: ')).upper().strip()
    print('-' * 30)
    if sexo == 'F' and idade < 20:
        mulheres+=1
    if sexo == 'M':
        homens+=1
    if idade>18:
        maiores+=1
    resp = ' ' #tem q ter o espaco
    while resp != 'S' and 'N': #validando, enquanto resp for diferente de s ou n continue a perguntar
        resp = str(input('Deseja continuar [S|N]: ')).upper().strip()
    if resp == 'N':
        break;
print(f'Há {mulheres} mulheres com menos de 20 anos.')
print(f'Há {homens} homens.')
print(f'Há {maiores} com mais de 18 anos.')

#SE DIGITAR LETRA NO LUGAR DE IDADE E NUMERO NO LUGAR DE SEXO TEM Q FICAR PEDINDO