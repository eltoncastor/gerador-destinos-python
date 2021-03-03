from modules.interface import *

def lerNum(msg='Sua opção: '):
    from time import sleep
    lista = list()
    while len(lista) < 3:
        num = int(input(msg+': '))
        if num in lista:
            print("Esse número já foi adicionado.")
        else:
            lista.append(num)
        if len(lista) < 3:
            if not continuar():
                break
    return lista


def continuar():
    from time import sleep
    while True:
        sleep(0.4)
        separadorSimples()
        continuar = str(input('Mais um destino? "s" para sim [s/n] '))
        if continuar in 'sS':
            return True
        elif continuar in 'nN': 
            return False
        else: print('\n\033[31m[ERRO] Responda com "s" para SIM ou "n" para NÃO.\033[m')


def stop():
    from time import sleep
    while True:
        continuar = str(input('Deseja sair? Digite "s" para sair [s/n] '))
        if continuar in 'sS':
            separadorSimples()
            print('OK!')
            sleep(0.5)
            print('Saindo do programa...')
            sleep(1)
            separador()
            print('Programa finalizado!')
            separador()
            return True
        elif continuar in 'nN': 
            separadorSimples()
            print('OK!')
            sleep(0.5)
            print('Retornando ao MENU PRINCIPAL...')
            sleep(0.5)
            separador()
            sleep(1)
            return False
        else: 
            print('\n\033[31m[ERRO] Responda com "s" para SIM ou "n" para NÃO.\033[m\n')