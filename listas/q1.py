def A(lista: list):
    maiorElemento = -999999

    for elemento in lista:
        if elemento >= maiorElemento:
            if type(elemento) == list:
                retorno = A(elemento)
                if retorno > maiorElemento:
                    maiorElemento = retorno
            elif elemento > maiorElemento:
                maiorElemento = elemento
    return maiorElemento


def B(lista: list):
    soma = sum(lista)
    return soma


def C(lista: list):
    return lista.count(1)


def D(lista: list):
    lista_positive = lista[9:19] * 1
    soma_items = B(lista_positive)
    number_elements_list = len(lista)

    media = soma_items / number_elements_list

    return media



def E(lista: list):
    pass


def F(lista: list):
    pass


def G(lista: list):
    pass


# Testes
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

func_num = 0

funcs = [A(lista), B(lista), C(lista), D(lista), E(lista), F(lista), G(lista)]
for f in funcs:
    func_num += 1
    print(f"Função {func_num}:", f)
