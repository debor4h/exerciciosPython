produtos = ('Lápis',1.78,'Borracha',0.50,'Caderno',25.56,'Mochila',40.90,'Apontador',0.50,'Régua',5.67)
for i,v in enumerate(produtos):
    if i%2==0:
        print(f'{v:.<32}R$',end = '') #end coloca na msm linha
    elif i%2!=0:
        print(f'{v:.2f}') #para aparecer com 2 casas decimais
#.<32 ele ajusta o txt deixa centralizado, ele vai colocar os pontos

