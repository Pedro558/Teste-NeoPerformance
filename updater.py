import pandas as pd

# Make the 'df_vendas' DataFrame global
global df_vendas

# Read actual data
df_vendas_atual = pd.read_csv('vendas.xls')

# Check if the 'df_vendas' DataFrame is already defined
if 'df_vendas' not in globals():
    df_vendas = df_vendas_atual 
    print("DataFrame 'df_vendas' defined by first time.")
elif not df_vendas_atual.equals(df_vendas):
    df_vendas = df_vendas_atual
    print("Dados atualizados com sucesso!")
