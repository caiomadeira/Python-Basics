nome = 'boa tarde!'
ind = -1
cont = 0
fim = -len(nome)

while ind >=fim and nome[ind] != ' ':
     cont=cont+1
     ind = ind - 1

print(cont)