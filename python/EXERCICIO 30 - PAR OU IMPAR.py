#e par ou impar
import time
from datetime import datetime
dh = datetime.now() #data

print(dh.strftime('DATA: %d/%m/%Y HORA: %H:%M'))
x = int(input('\033[32mDigite um número:\033[32m '))
print('\033[34mPROCESSANDO...\033[34m')
time.sleep(2) #temporalizador
if (x%2)==0:
    print('\033[36mPar\033[36m') # cor nas letras
else:
    print('\033[31mÍmpar\033[31m')