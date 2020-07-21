# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pandas as pd

dados = pd.read_csv('base_pizzaria.csv', header=None)
del dados[3]
del dados[4]
del dados[2]
del dados[6]
transacoes = []
for i in range(0,2244):
    transacoes.append([str(dados.values[i,j]) for j in range(0,3)])
    
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