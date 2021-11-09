#from apyori import apriori
from fpgrowth_py import fpgrowth
from efficient_apriori import apriori
import pandas as pd
import csv


minSup = 0.5
minConf = 0.5


df = pd.read_csv('teste - Página1.csv')

transactions_from_df = [tuple(row) for row in df.values.tolist()]
itemsets, results = apriori(transactions_from_df, min_support=0.5, min_confidence=1,max_length=2)
freqItemSet, rules = fpgrowth(transactions_from_df, minSup, minConf, )


with open('teste.txt','w') as arquivo:
    for valor in results:
        arquivo.write(str(valor) + '\n')
    for valor in rules:
        arquivo.write(str(valor) + '\n')



