# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:28:16 2020

@author: PICHAU
"""

import pandas as pd

dados = pd.read_csv('vestibular.csv', header=None)

transacoes = []
for i in range(0,1326):
    transacoes.append([str(dados.values[i,j]) for j in range(0,19)])
    
from apyori import apriori

regras = apriori(transacoes, min_support = 0.003, min_confidence= 0.2, min_lift = 2.0, min_lenght=2)
#regras = apriori(transacoes)

resultados = list(regras)

#print(resultados)

resultados2 = [list(x) for x in resultados]

#print(resultados2)

resultadoformatado = []

for j in range(0,3):
    resultadoformatado.append([list(x) for x in resultados2[j][2]])
print(resultadoformatado)