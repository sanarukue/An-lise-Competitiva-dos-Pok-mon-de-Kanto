import pandas as pd

# Carregar o dataset
df = pd.read_csv('pokemon_kanto.csv')

# Criar colunas de ofensiva e defensiva
df['total_offense'] = df['attack'] + df['special-attack']
df['total_defense'] = df['defense'] + df['special-defense']

# Mostrar Top 10 ofensivos
print("Top 10 Pokémon ofensivos:")
print(df[['name', 'total_offense']].sort_values(by='total_offense', ascending=False).head(10))

# Mostrar Top 10 defensivos
print("\nTop 10 Pokémon defensivos:")
print(df[['name', 'total_defense']].sort_values(by='total_defense', ascending=False).head(10))
