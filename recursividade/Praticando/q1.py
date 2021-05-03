"""
Escreva  uma  função  recursiva  que  receba  um  número  inteiro  como  parâmetro  e  retorne  a quantidade  de
vezes  que  os algarismos 3 e 4 aparecem no número. Exemplo: se o número for 239424, a função retornará 3.

"""


# n % 10 --> sempre é o ultimo digito do numero
# n // 10 --> o numero sem o ultimo digito


# Escopo da função
def qtdAlgoritmos(n):
    # caso base
    if n < 10:
        if n == 3 or n == 4:
            return 1  # para cada 3 e 4 ele vai retornar a quantidade existente, no caso 1
        else:
            return 0  # caso o numero seja maior que 10 ele retorna 0

    # caso recursivo
    if n % 10 == 3 or n % 10 == 4: # se o ultimo algoritimo (n % 10) for 3 ou 4
        return 1 + qtdAlgoritmos(n // 10) # retorna a quantidade o numero sem o ultimo algoritimo e soma mais 1 ao contador de Tres e Quatros
    else:
        return qtdAlgoritmos(n // 10) # caso nao seja, retorna o algoritmo sem o numero e nao soma nada ao acontador


# Testes // Chamada das funções
print(qtdAlgoritmos(n=44344))
