import pandas as pd
import numpy as np
from pathlib import Path
from os import listdir
from os.path import isfile, join




def trataDataSet():

    df = pd.read_csv(r"C:\\Users\\SirAxe\\Desktop\\Apyori\\ConsolidadoUnicoChamador.csv", sep=';',
                     names=["projeto", "arquivo", "chamador", "chamado", "biblioteca", "tipo", "inutil"])

    antigo = df
    pd.set_option("display.max_colwidth", None)
    df = df.iloc[1:, 0:6]
    df = df[~df["tipo"].isin(["Indeterminada"])]

    df["chamadora"] = df["projeto"] + "@" + df["arquivo"] + "@" + df["chamador"]

    # with open ("testeData.csv", 'w') as file:
    df.to_csv("testeData.csv", sep=";", columns=["chamadora", "chamado"], index=False)


trataDataSet()

