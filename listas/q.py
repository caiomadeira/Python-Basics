#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exibir os nomes dos alunos por nota
Alunos que tiraram 0

Alunos que tiraram 1

Alunos que tiraram 2

Notas = int[0, ... , 10]
"""


def principal(alunos):
    notas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    nomesAlunos = []

    for aluno in alunos:
        # alunos que tiraram 0
        notas_aluno = aluno[2]  # indice 2 = notas int
        nome_aluno = aluno[1]  # indice 1 = nome string
        # nomesAlunos.append(nome_aluno)
        if notas_aluno == notas[0]:
            nomesAlunos.append(nome_aluno)

    for nome, indice in enumerate(nomesAlunos):
        print(f"Alunos que tiraram x: {nome, indice}")

    # lista_notas = [[], [], [], [], [], [], [], [], [], [], []]
    #
    # for aluno in alunos:
    #     notas = aluno[2]
    #     nome = aluno[1]
    #     lista_notas[notas].append(nome)
    #
    # print(f"Alunos que tiraram X: {lista_notas}")


alunos = [
    [807238, "Abrilina Decima Nona Cacapavana Piratininga de Almeida", 1],
    [424646, "Abxivispro Jacinto", 7],
    [251403, "Acheropita Papazone", 10],
    [505965, "Adalgamir Marge", 0],
    [508527, "Adegesto Pataca", 0],
    [432986, "Adoracao Arabites", 4],
    [707788, "Aeronauta Barata", 6],
    [432624, "Agricola Beterraba Areia Leao", 2],
    [769434, "Agricola da Terra Fonseca", 9],
    [345610, "Alce Barbuda Aldegunda Carames More", 3],
    [198330, "Aleluia Sarango", 8],
    [237823, "Alfredo Prazeirozo Texugueiro", 1],
    [621386, "Alma de Vera", 9],
    [486374, "Amado Amoroso", 10],
    [377879, "Amazonas Rio do Brasil Pimpao", 5],
    [790160, "America do Sul Brasil de Santana", 2],
    [279139, "Amin Amou Amado", 2],
    [924392, "Amor de Deus Rosales Brasil", 10],
    [528369, "Anatalino Reguete", 8],
    [507168, "Antonio Americano do Brasil Mineiro", 0],
    [342902, "Antonio Dodoi", 10],
    [778704, "Antonio Manso Pacifico de Oliveira Sossegado", 3],
    [366299, "Antonio Melhoranca", 9],
    [689762, "Antonio Morrendo das Dores", 2],
    [226647, "Antonio Noites e Dias", 1],
    [348890, "Antonio P. Testa", 9],
    [801446, "Antonio Pechincha Antonio Querido Fracasso", 4],
    [164294, "Antonio Treze de Junho de Mil Novecentos e Dezessete", 1],
    [695758, "Apurina da Floresta Brasileira", 6],
    [462622, "Araci do Precioso Sangue", 1],
    [773807, "Argentino Argenta", 3],
    [573304, "Aricleia Cafe Cha", 10],
    [192716, "Armando Nascimento de Jesus", 9],
    [210273, "Arquibaldo Nana do Mercado", 10],
    [755285, "Arquiteclinio Petrocoquinio de Andrade", 1],
    [621690, "Asteroide Silverio", 2],
    [409098, "Bananeia Oliveira de Deus", 0],
    [490111, "Bandeirante do Brasil Paulistano", 10],
    [915810, "Barrigudinha Seleida", 3],
    [877825, "Benedito Autor da Purificacao", 8],
    [223918, "Benedito Camurca Aveludado", 4],
    [828170, "Benedito Froscolo Jovino de Almeida Aimbare Militao de Souza Baruel de Itaparica Bore Fomi de Tucunduva",
     6],
    [827639, "Benigna Jarra Benvindo Viola", 0],
    [670925, "Bispo de Paris", 9],
    [528823, "Bizarro Assada Boaventura Torrada", 0],
    [266195, "Bom Filho Persegonha", 0],
    [984444, "Brandamente Brasil", 7],
    [647348, "Brasil Washington C. A. Junior", 4],
    [245345, "Brigida de Samora Mora Belderagas Piruegas", 9],
    [731135, "Cafiaspirina Cruz", 8],
    [676969, "Capote Valente e Marimbondo da Trindade", 1],
    [442101, "Caius Marcius Africanus", 5],
    [572824, "Carabino Tiro Certo", 1],
    [909313,
     "Carlos Alberto Santissimo Sacramento Cantinho da Vila Alencar da Corte Real Sampaio Carneiro de Souza e Faro", 5],
    [248858, "Caso Raro Yamada", 10],
    [429390, "Ceu Azul do Sol Poente", 3],
    [959177, "Chananeco Vargas da Silva", 5],
    [518498, "Chevrolet da Silva Ford", 4],
    [467776, "Cincero do Nascimento", 5],
    [691158, "Cinconegue Washington Matos", 8],
    [954071, "Clarisbadeu Braz da Silva", 6],
    [894786, "Colapso Cardiaco da Silva", 8],
    [719585, "Comigo e Nove na Garrucha Trouxada", 6],
    [171915, "Confessoura Dornelles", 9],
    [417519, "Crisoprasso Compasso", 6],
    [733980, "Danubio Tarada Duarte", 9],
    [640892, "Darcilia Abracos de Carvalho Santinho", 6],
    [675751, "Deus Magda Silva Deus e Infinitamente Misericordioso", 4],
    [907280, "Deus Quer Magalhaes Mota", 5],
    [261466, "Deusarina Venus de Milo", 9],
    [447430, "Dezencio Feverencio de Oitenta e Cinco", 3],
    [781667, "Dignatario da Ordem Imperial do Cruzeiro", 6],
    [462535, "Dilke de La Roque Pinho", 3],
    [198642, "Disney Chaplin Milhomem de Souza", 6],
    [676231, "Dolores Fuertes de Barriga", 10],
    [608278, "Dosolina Piroca Tazinasso", 9],
    [999907, "Dragica Broko", 2],
    [816848, "Ernesto Segundo da Familia Lima Esdras Esdron Eustaquio Obirapitanga", 4],
    [964027, "Esparadrapo Clemente de Sa", 2],
    [402124, "Espere em Deus Mateus", 2],
    [912641, "Estacio Ponta Fina Amolador", 0],
    [470709, "eter Sulfurico Amazonino Rios", 5],
    [565104, "Excelsa Teresinha do Menino Jesus da Costa e Silva", 8],
    [653393, "Farao do Egito Sousa", 9],
    [162826, "Fedir Lenho", 10],
    [462205, "Felicidade do Lar Brasileiro", 5],
    [652718, "Finolila Piaubilina", 2],
    [773290, "Flavio Cavalcante Rei da Televisao", 2],
    [148928, "Francisco Notorio Milhao", 6],
    [334744, "Francisco Zebedeu Sanguessuga", 6],
    [833741, "Francisoreia Doroteia Dorida", 4],
    [890005, "Fridundino Eulâmpio", 9],
    [649746, "Gerunda Gerundina Pif Paf", 7],
    [245029, "Gigle Catabriga", 6],
    [896251, "Graciosa Rodela D'alho", 6],
    [912170, "Heubler Janota", 0],
    [785179, "Hidraulico Oliveira", 10],
    [784588, "Himineu Casamenticio das Dores Conjugais", 4],
    [156917, "Holofontina Fufucas", 9],
    [645080, "Homem Bom da Cunha Souto Maior", 8],
    [796067, "Horinando Pedroso Ramos", 1],
    [792649, "Hugo Madeira de Lei Aroeiro", 10],
    [931450, "Hypotenusa Pereira", 6],
    [921817, "Ilegivel Inilegivel", 5],
    [418744, "Inocencio Coitadinho", 4],
    [196464, "Isabel Defensora de Jesus", 10],
    [369344, "Izabel Rainha de Portugal", 9],
    [340053, "Jacinto Fadigas Arranhado", 8],
    [751581, "Janeiro Fevereiro de Marco Abril", 3],
    [395596, "Joao Bispo de Roma Joao Cara de Jose", 5],
    [986239, "Joao Colica", 6],
    [841541, "Joao da Mesma Data", 7],
    [324484, "Joao de Deus Fundador do Colto", 1],
    [203528, "Joao Meias de Golveias", 4],
    [702992, "Joao Pensa Bem", 1],
    [533933, "Joao Sem Sobrenome", 10],
    [815186, "Joao Suino de Oliveira", 2],
    [618011, "Jose Amâncio e Seus Trinta e Nove", 2],
    [850539, "Jose Casou de Calcas Curtas", 5],
    [938952, "Jose Catarrinho", 10],
    [548184, "Jose Machuca", 4],
    [580766, "Jose Maria Guardanapo", 5],
    [104649, "Jose Padre Nosso", 0],
    [431958, "Jovelina o Rosa Cheirosa", 1],
    [855928, "Jotaca Dois Mil e Um", 2],
    [774689, "Juana Mula Julio Santos Pe-Curto", 9],
    [852319, "Justica Maria de Jesus", 6],
    [448388, "Lanca Perfume Rodometalico de Andrade", 2],
    [854934, "Leao Rolando Pedreira", 7],
    [859755, "Leda Prazeres Amante", 6],
    [259973, "Letsgo da Silva", 5],
    [936159, "Liberdade Igualdade Fraternidade Nova York Rocha", 5],
    [307713, "Libertino Africano Nobre", 9],
    [847742, "Lindulfo Celidonio Calafange de Tefe", 3],
    [892759, "Lynildes Carapunfada Dores Figado", 2],
    [452104, "Magnesia Bisurada do Patrocinio", 6],
    [101117, "Manganes Manganesfero Nacional", 3],
    [322028, "Manolo Porras y Porras Manoel de Hora Pontual", 8],
    [567368, "Manoel Sovaco de Gambar", 0],
    [107376, "Manuel Sola de Sa Pato", 0],
    [846280, "Manuelina Terebentina Capitulina de Jesus Amor Divino", 10],
    [340124, "Marciano Verdinho das Antenas Longas", 10],
    [760414, "Maria Constanca Dores Panca", 7],
    [575714, "Maria da Cruz Rachadinho", 10],
    [976541, "Maria da Segunda Distracao", 2],
    [245686, "Maria de Seu Pereira", 0],
    [197639, "Maria Felicidade", 3],
    [878658, "Maria Humilde", 4],
    [726552, "Maria Maquina", 4],
    [541949, "Maria Panela Maria Passa Cantando", 4],
    [523840, "Maria Privada de Jesus", 8],
    [275645, "Maria-voce-me-mata da Silva", 3],
    [519743, "Mario de Seu Pereira", 1],
    [467611, "Meirelaz Assuncao", 2],
    [118289, "Mimare indio Brazileiro de Campos", 3],
    [212383, "Ministeio Salgado", 5],
    [430074, "Naida Navinda Navolta Pereira", 0],
    [851658, "Napoleao Estado do Pernambuco", 9],
    [591065, "Napoleao Sem Medo e Sem Macula", 4],
    [177278, "Natal Carnaval Necroterio Pereira da Silva", 6],
    [598597, "Novelo Fedelo", 10],
    [772935, "Oceano Atlântico Linhares", 5],
    [802450, "Oceano Pacifico", 3],
    [274131, "Olinda Barba de Jesus", 10],
    [638986, "Orquerio Cassapietra", 8],
    [909814, "Otavio Bundasseca", 5],
    [596301, "Pacifico Armando Guerra", 8],
    [640703, "Padre Filho do Espirito Santo Amem", 6],
    [764297, "Palia Pelia Polia Pulia dos Guimaraes Peixoto", 8],
    [550670, "Paranahyba Pirapitinga Santana", 0],
    [296515, "Pedra da Penha", 10],
    [805476, "Pedrinha Bonitinha da Silva", 5],
    [550985, "Percilina Pretextata Predileta Protestante", 8],
    [553853, "Peta Perpetua de Ceceta", 3],
    [480974, "Placenta Maricornia da Letra Pi", 7],
    [256828, "Placido e Seus Companheiros", 1],
    [861653, "Pombinha Guerreira Martins", 10],
    [270710, "Primeira Delicia Figueiredo Azevedo", 10],
    [372351, "Primavera Verao Outono Inverno", 2],
    [728739, "Produto do Amor Conjugal de Maricha e Maribel", 7],
    [584863, "Protestado Felix Correa", 1],
    [413565, "Radigunda Cercena Vicensi", 8],
    [187128, "Remedio Amargo", 9],
    [446825, "Renato Pordeus Furtado", 2],
    [885223, "Ressurgente Monte Santos", 5],
    [407432, "Restos Mortais de Catarina", 8],
    [892028, "Rita Marciana Arroteia", 10],
    [303001, "Rolando Caio da Rocha", 4],
    [740040, "Rolando Escadabaixo", 7],
    [745766, "Romulo Reme Remido Rodo", 7],
    [326611, "Safira Azul Esverdeada", 8],
    [608664, "Sebastiao Salgado Doce", 6],
    [181526, "Segundo Avelino Peito", 3],
    [749451, "Sete Chagas de Jesus e Salve Patria", 8],
    [110278, "Sete Rolos de Arame Farpado", 2],
    [679921, "Simplicio Simplorio da Simplicidade Simples", 2],
    [309360, "Soraiadite das Duas a Primeira ", 8],
    [408120, "Telesforo Veras", 1],
    [870878, "ultimo Vaqueiro", 1],
    [846694, "Um Dois Tres de Oliveira Quatro", 9],
    [390099, "Um Mesmo de Almeida", 10],
    [120822, "Universo Cândido", 0],
    [213995, "Usnavy da Silva", 0],
    [999007, "Valdir Tirado Grosso", 9],
    [546932, "Veneza Americana do Recife", 3],
    [975832, "Vicente Mais ou Menos de Souza", 4],
    [761841, "Vitoria Carne e Osso", 3],
    [289788, "Vitimado Jose de Araujo", 7],
    [369705, "Vitor Hugo Tocagaita", 6],
    [851100, "Vivelinda Cabrita", 0],
    [711060, "Voltaire Rebelado de Franca", 10],
]

principal(alunos=alunos)
