ano = int(input("Ano de nascimento: "))
sexo = str(input("Qual seu sexo F ou M: ")).upper().strip()
idade = 2021 - ano; #date.today().year - funcao do pc para saber o ano atual
if sexo == 'F':
    print("Você não precisa se alistar, pois é mulher.")
elif(idade<18):
    print("Ainda vai ter que se alistar, pois a idade é de: {} anos.\nFalta {} anos para se alistar.".format(idade,18-idade))
elif(idade==18):
    print("Se alista agora.")
else:
    print("Já passou {} ano de se alistar.".format(idade-18))