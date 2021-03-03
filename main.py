from modules.interface import * 
from modules.countries import destino
from modules.functions import *
from os import system
from time import sleep

while True:
    system('cls') # limpa o terminal
    
    titulo('Gerador de países para viajar')
    msg('Continente')
    menu(['Europa','Ásia', 'América'])
    quebraLinha()
    continente = lerNum('Digite o n° do continente')
    gerandoPaises()

    system('cls') # limpa o terminal
    
    titulo('Destino(s) gerado(s)')
    sleep(0.4)
    quebraLinha()
    ol(destino(continente))
    sleep(0.5)
    separador()

    if stop():
        break 
    
    





