# a funcao recebe um inteiro e retorna um inteiro
def fatorial(n):
    # caso base
    if n == 1:
        return 1
    # caso recursivo - a função SEMPRE chama a si própria
    return n * fatorial(n - 1)  # fazemos o numero recebido menos seu antecessor ate que chegue aao valor 1 e retorne 1


print(fatorial(n=5))

# callstack - pilha de chamada

# toda vez que chamo uma função, ela entra na pilha de chamada com o scopo salvo na memoria entao
# tudo dentro dela é salvo na memoria e quando ela retorna um valor ela saiu do callstack
