import pandas as pd
import sys
sys.path.append('../')
from src import sp_limpieza as sl

def exploracion_df_abtesting(df,columna_control):
    for categoria in df[columna_control].unique():
        display(categoria)
        df_filtrado = df[df[columna_control] == categoria]
        display(df_filtrado.describe().T)