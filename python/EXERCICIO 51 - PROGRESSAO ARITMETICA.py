a1 = int(input("Escolha o primeiro número A1: "))
r = int(input("Escolha de quantos em quantos quer pular R: "))
decimo  = a1 + (10-1) *r #no 10 vc coloca o termo que vc quer
for pa in range(a1,decimo + r,r):
    print(pa) #progressao aritmetica

#a1 e o primeiro termo
#r é razão