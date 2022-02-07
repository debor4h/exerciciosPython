n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1+n2)/2
if(media < 5.0):
    print("Reprovado, sua média {:.2f}".format(media))
elif(media <=6.9):
    print("Recuperação, sua média {:.2f}".format(media))
else:
    print("Aprovado, sua média {:.2f}".format(media))