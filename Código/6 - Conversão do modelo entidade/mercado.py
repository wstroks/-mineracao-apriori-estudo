# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:44:23 2020

@author: PICHAU
"""
import pymysql

conexao = pymysql.connect(host='localhost', user='root', password='secret', db='mercado')

cursorVendas = conexao.cursor()
#cursor.execute('select * from produtos');
cursorVendasProdutos = conexao.cursor()
base = ''
cursorVendas.execute('select * from vendas')
for vendas in cursorVendas:
    print(vendas)
    quantidade = cursorVendasProdutos.execute('select prd.nome from mercado.venda_produtos vpr inner join produtos prd on vpr.idproduto = prd.idproduto where vpr.idvenda = ' + str(vendas[0]))
    i = 1
    for produtos in cursorVendasProdutos:
        print(produtos)
        if(i==quantidade):
            base = base + produtos[0]
        else:
            base = base + produtos[0] +','
        i=i+1
    base =base + '\n'
arquivo = open('base_importada.csv', 'w')
arquivo.write(base)
arquivo.close()

cursorVendas.close()
cursorVendasProdutos.close()
conexao.close()