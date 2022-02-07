#r e razao de quantos em quantos vai pular
#pa e a subtracao da razao com o seu anterior, ex razao é 2 ,
a1= int(input('Indique o primeiro termo da PA: '))
r = int(input('Indique a razão da PA: '))
an = a1 + (10-1)*r #esse -1 e da formula, aqui vai dar 20 se colocar em p 2 e em r 2
#an = 2+9*2=20
while a1 <= an:#enquanto 2 for menor ou igual a 20 faca
    print(a1, end=' ')#aqui e para mostrar a1 pq e ele que recebe o incremento
    a1 += r #a1 + razao pq ele tem q por o incremento de acordo com a razao pedida, ate acalcar 20
print('FIM')


#progressao aritmetica mostrar os 10 primeiros termos
#an=a1 + r·(n-1)  FORMULA

#N→ é a posição do termo;

#a1→ é o primeiro termo;

#r → razão.
c = 1
print('PROGRESSÃO ARITMÉTICA')
primeiro_termo = int(input('Qual o primeiro termo (a1): '))
razao = int(input('Qual a razão (r): '))
n = primeiro_termo + razao *(10-1)
for n in range(primeiro_termo, n+1 , razao):
  print(n,end = ' ')


print()
print('*'*50)
print()
while c <= 10:
  print(primeiro_termo,end = '')
  if c<10:
    print(end = '->')
  primeiro_termo+=razao
  c+=1
