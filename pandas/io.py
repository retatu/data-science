import numpy as np
import pandas as pd

df = pd.read_csv('csv.csv', sep=',')
print(df)

#para exportar
df.to_excel('ex.xlsx', sheet_name='sheet1')

#Le um de um arquivo excel
df = pd.read_excel('ex.xlsx', sheet_name='sheet1')
print(df)

#Para ler páginas web
df = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
#O retorn é uma lista
print(type(df))
#Aqui é um df
print(type(df[0]))
print(df[0]['Bank Name'])
