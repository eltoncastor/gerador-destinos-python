def destino(lista):
    from random import choice

    paises = [['Itália', 'Suíça', 'Noruega', 'França', 'Alemanha', 'Portugal', 'Rússia', 'Holanda', 'Grécia', 'Croácia', 'Romênia', 'Ucrânia'], ['Japão', 'China', 'Coreia do Sul', 'Singapura', 'Butão', 'Indonésia', 'Tailândia', 'Índia', 'Afeganistão'], ['Brasil', 'Estados Unidos', 'México', 'Argentina', 'Chile', 'Equador', 'Cuba', 'Bahammas', 'Panamá', 'Honduras', 'Porto Rico']]

    gerados = []
    for item in lista:
        if int(item) == 1:
            gerados.append(choice(paises[0]))
        if int(item) == 2:
            gerados.append(choice(paises[1]))
        if int(item) == 3:
            gerados.append(choice(paises[2]))
    return gerados

