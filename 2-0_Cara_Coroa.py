# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:50:46 2021
Program: Cara_Coroa
@author: Fabio Batista ROdrigues
"""
# Este programa tem como objetivo avaliar a aleatoriedade da bibliotexa random ao mesmo tempo
# que faz uma brincadeira usando sorteios aleatorios de cara coroa.

# Importaçao de bibliotecas
from tqdm import tqdm
import random

if __name__ == '__main__':
    # Passo1. Entrada - Numeros de sorteios
    tam = int(input("Entre com o numero de sorteios da moeda: "))
    sorteios = [] * tam
    largura = range(0, tam)
    for i in tqdm(largura, colour='blue', desc='Fazendo os sorteios'):
        # Sorteio das tam possibilidades
        cara_coroa = random.randrange(0, 2)
        # Armazenar cada sorteio numa lista de tamanho tam
        sorteios.append(cara_coroa)
    # Analisar Quantas vezes aparece o numero zero correspondente a coroa
    # e o numero 1, correspondente a cara
    coroa = 0
    cara = 0
    for i in tqdm(range(0, tam), colour='green', desc = 'Processando'):
        if sorteios[i] == 0:
            coroa += 1
        elif sorteios[i] == 1:
            cara += 1
    # Analisar a porcentagem de cada sorteio
    Porcent_coroa = (coroa / tam) * 100
    Porcent_cara = (cara / tam) * 100

    # Imprimir a mensagem correspondente
    print(
        """\n     Cara = {0:d} e Coroa = {1:d}
             Isso é equivalente a:
             Coroa = {2:.2f} %
             Cara  = {3:.2f} %""".format(cara, coroa, Porcent_coroa, Porcent_cara))