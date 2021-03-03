def titulo(msg, tam=50):
    from time import sleep
    sleep(0.3)
    linha()
    quebraLinha()
    sleep(0.4)
    print(msg.center(tam))
    quebraLinha()
    sleep(0.3)
    linha()


def quebraLinha():
    print('')


def linha(tam=50):
    print('='*tam)


def linhaSimples():
    print('-'*50)


def separadorSimples():
    quebraLinha()
    linhaSimples()
    quebraLinha()


def separador():
    quebraLinha()
    linha()
    quebraLinha()


def msg(msg, tam=50):
    print(('-'*len(msg)).center(tam))
    print(msg.center(tam))
    print(('-'*len(msg)).center(tam))


def gerandoPaises():
    from time import sleep
    quebraLinha()
    sleep(0.5)
    linhaSimples()
    quebraLinha()
    sleep(0.8)
    print('Gerando países...'.center(50))
    sleep(0.5)
    quebraLinha()
    linhaSimples()
    sleep(1.2)


def menu(lista):
    for posição, item in enumerate(lista):
        print(f'[{posição+1}] - {item}')
    linha()


def ol(lista):
    for posição, item in enumerate(lista):
        print(f'({posição+1:<}) -> {item.center(38)}')



        


