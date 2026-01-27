import pandas as pd
pd.set_option('display.max_columns', None)
df =pd.read_csv('../MODULO AB TESTING AMAZON/amazon_abtesting/data/data_raw.csv')

print("Análisis Exploratorio de Datos Preliminar")

eda_preliminar(df)

def eda_preliminar(df):
    display(df.sample(5))
    print(f"Nuestro conjunto de datos tiene {df.shape[0]} filas y {df.shape[1]} columnas")
    df.info()
    df.isnull().sum()
    round(df.isnull().mean()*100,2)
    df.duplicated().sum()
    df.select_dtypes(include="object").columns
    for col in df.select_dtypes(include="object").columns:
        print(df[col].value_counts())