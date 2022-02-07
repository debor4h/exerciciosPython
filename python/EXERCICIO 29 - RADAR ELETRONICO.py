#receber 7 de multa por cada km rodado acima do limite
import time
from datetime import datetime

data_hora = datetime.now()
print(data_hora.strftime('%d/%m/%Y %H:%M'))
km = int(input('Qual a velocidade do carro:'))
print('Processando.....')
time.sleep(2) #pc vai parar por 2 segundos
if km >80:
    print('Multado, a multa é de: R$',(km-80)*7)
else:
    print('Velocidade do carro é de: {} . Boa viagem!!!'.format(km))

print('-'*50)

vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
  multa = (vel - 80 )* 7.00
  print(f'\033[1;31mMultado! Você excedeu o limite permitido que é de 80 KM/H\nVocê deve pagar uma multa de\033[m \033[1;33mR${multa :.2f}!\033[m')
print('\033[1;33mTenha um bom dia! Dirija com segurança!\033[m')