import pandas as pd
import sys
sys.path.append('../')
from src import sp_limpieza as sl

def minusglobal(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower() 
        
def espaciosguiones(df,col):
    df[col]= df[col].str.replace(' ','_')
    df.sample(5)