
import pandas as pd

# Carregar o dataset
df = pd.read_csv('netflix_titles.csv')

# Exibir as primeiras 5 linhas do dataset
print('Primeiras 5 linhas do dataset:')
print(df.head())

# Exibir informações gerais sobre o dataset (tipos de dados, valores não nulos)
print('\nInformações gerais do dataset:')
print(df.info())

# Exibir estatísticas descritivas para colunas numéricas
print('\nEstatísticas descritivas do dataset:')
print(df.describe())

# Contar valores nulos por coluna
print('\nValores nulos por coluna:')
print(df.isnull().sum())

# Contar o número de valores únicos em cada coluna
print('\nNúmero de valores únicos por coluna:')
print(df.nunique())

# Contar a ocorrência de cada tipo de conteúdo (filme/série)
print('\nContagem de tipos de conteúdo:')
print(df['type'].value_counts())

# Contar os 10 principais países de produção
print('\nTop 10 países de produção:')
print(df['country'].value_counts().head(10))

# Contar os 10 principais diretores
print('\nTop 10 diretores:')
print(df['director'].value_counts().head(10))

# Contar os 10 principais gêneros/listados_em
print('\nTop 10 gêneros/listados_em:')
print(df['listed_in'].value_counts().head(10))


