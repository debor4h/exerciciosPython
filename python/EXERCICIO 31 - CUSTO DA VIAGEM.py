#distancia da viagem em km, 0.5 por cada km de viagens de ate 200 e 0.45 p mais longas
from datetime import datetime
import time
dh = datetime.now()
print(dh.strftime('DATA: %d/%m/%Y e %H:%M'))
dist = int(input('Qual KM da viagem? '))
if dist<=200:
    print('Preço a pagar:R$ {} por {}KM rodado.'.format(0.50*dist,dist))
else:
    print('Preço a pagar:R$ {} por {}KM rodado.'.format( 0.45*dist,dist))
