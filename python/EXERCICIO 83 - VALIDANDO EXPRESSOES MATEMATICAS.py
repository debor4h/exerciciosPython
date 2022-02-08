#nao entendi
#solucao guanabara
expr = str(input('Expressão: '))
pilha = []
for s in expr:
    if s == '(':
        pilha.append('(')
    elif s == '(':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break;
if len(pilha) == 0:
    print('Válida')
else:
    print('inválida')


#((a*f)+(aaa)))-a(njhg or (a+b)+((a+b)+a)teste