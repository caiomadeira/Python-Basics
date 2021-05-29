arq = open('dados.txt', 'w+')
while True:
    nome = input()
    if not nome:
        break
    arq.write(nome + '\n')


arq.close()