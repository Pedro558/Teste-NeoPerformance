# import 'pandas' library
import pandas as pd
import updater

df_vendas = updater.df_vendas

# verify the data types
df_vendas.dtypes

# rename the 'data' column
df_vendas = df_vendas.rename(columns={'data_venda': 'data'})

# convert 'data' to 'datatype'
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# check for missing values
if df_vendas.isna().any().any():
  df_vendas = df_vendas.fillna(0)


# create a new column
df_vendas['receita_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']

# Create 'mês' column
df_vendas['mês'] = df_vendas['data'].dt.month

# Function to categorize sellers based on quantity sold
def categorize_seller(qntd):
  if qntd > 100:
    return 'Vendedor Destaque'
  elif qntd > 50:
    return 'Vendedor Médio'
  else:
    return 'Vendedor Iniciante'
  
# Calling function and create a new column
df_vendas['categoria_vendedor'] = df_vendas['quantidade'].apply(categorize_seller)

# Export dataframe
df_vendas.to_csv('./tabelas_tratadas/vendas_tratadas.csv', index=False)

