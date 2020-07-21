# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:46:02 2020

@author: PICHAU
"""

import matplotlib.pyplot as plt
from numpy import genfromtxt

#dados = genfromtxt('valor_total.csv')
#histograma = plt.hist(dados, bins='sturges')
#histograma = plt.hist(dados, bins='scott')
#histograma = plt.hist(dados, bins='fd')
#histograma = plt.hist(dados, bins='5')

#histograma = plt.hist(dados)

dados2 = genfromtxt('tempo_decorrido.csv')

histograma2 = plt.hist(dados2)
