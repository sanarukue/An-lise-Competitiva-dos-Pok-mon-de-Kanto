import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Config do streamlit
st.set_page_config(page_title="Pokémon de Kanto - Análise Competitiva", layout="wide")

# Carregamento Dados
df = pd.read_csv('pokemon_kanto.csv')

# Colunas adicionais para ataque total e defesa
df['total_offense'] = df['attack'] + df['special-attack']
df['total_defense'] = df['defense'] + df['special-defense']

# KMeans para definir tiers
cluster_features = df[['total_offense', 'total_defense', 'hp', 'speed']].copy()
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
df['tier'] = kmeans.fit_predict(cluster_features)


# Ordenar os tiers de forma interpretável
tier_mean = df.groupby('tier')[['total_offense', 'total_defense']].mean()
tier_order = tier_mean.sort_values(by=['total_offense', 'total_defense'], ascending=False).reset_index()
tier_map = {row['tier']: f"Tier {i+1}" for i, row in tier_order.iterrows()}
df['tier_label'] = df['tier'].map(tier_map)

# Cabeçalho e explicação
st.markdown("""
    <h1 style='text-align: center; color: #3366cc;'> Análise Competitiva dos Pokémon de Kanto</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <p style="font-size:16px;">
        Este dashboard auxilia o balanceamento competitivo, identificando os Pokémon com maior potencial ofensivo e defensivo.
        As categorias (Tiers) são definidas automaticamente via clusterização, considerando os atributos totais de ataque e defesa.
    </p>
""", unsafe_allow_html=True)

# Filtra o tipo
tipos = df['type1'].dropna().unique()
tipo_selecionado = st.multiselect(" Filtrar por Tipo Primário", sorted(tipos))
df_filt = df.copy()
if tipo_selecionado:
    df_filt = df[df['type1'].isin(tipo_selecionado)]

# Pokemons top 10 total ataque/defesa
col1, col2 = st.columns(2)
with col1:
    st.subheader(" Top 10 Ofensivos")
    st.dataframe(df_filt[['name', 'type1', 'total_offense']].sort_values(by='total_offense', ascending=False).head(10), use_container_width=True)

with col2:
    st.subheader(" Top 10 Defensivos")
    st.dataframe(df_filt[['name', 'type1', 'total_defense']].sort_values(by='total_defense', ascending=False).head(10), use_container_width=True)

# Gráfico de dispersão 
st.subheader(" Dispersão: Ofensiva vs Defensiva")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=df_filt,
    x='total_offense',
    y='total_defense',
    hue='tier_label',
    style='type1',
    palette='Set2',
    s=120,
    ax=ax
)
ax.set_xlabel('Ofensiva Total')
ax.set_ylabel('Defensiva Total')
ax.set_title('Pokémon de Kanto por Tier')

#  Joga a legenda pra direita do gráfico
ax.legend(title='Tier', bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(fig)
# Analise de tier
st.subheader(" Distribuição por Tier")
st.markdown("""
<ul>
<li><b>Tier 1</b>: Pokémon com maior poder ofensivo e/ou defensivo. Geralmente considerados desequilibrados.</li>
<li><b>Tier 2</b>: Muito fortes, mas com uma fraqueza visível.</li>
<li><b>Tier 3</b>: Pokémon medianos, equilibrados ou situacionais.</li>
<li><b>Tier 4</b>: Menor potencial competitivo, mas úteis em estratégias específicas.</li>
</ul>
""", unsafe_allow_html=True)

# Gráfico de barras com os iters
tier_counts = df['tier_label'].value_counts().sort_index()
st.bar_chart(tier_counts)

# Visualização de Pokémon por tier com "cards" do tier selecionado
tier_escolhido = st.selectbox(" Selecione um Tier para visualizar os Pokémon:", sorted(df['tier_label'].unique()))
st.dataframe(df[df['tier_label'] == tier_escolhido][[
    'name', 'type1', 'type2', 'hp', 'speed',
    'total_offense', 'total_defense', 'tier_label'
]].sort_values(by='total_offense', ascending=False), use_container_width=True)

st.subheader(" Cards dos Pokémon no Tier Selecionado")

df_tier = df[df['tier_label'] == tier_escolhido]

for idx in range(0, len(df_tier), 3):  # Mostrar 3 por linha
    row = df_tier.iloc[idx:idx+3]
    cols = st.columns(len(row))
    for i, (_, poke) in enumerate(row.iterrows()):
        with cols[i]:
            st.markdown(f"""
                <div style="border:1px solid #ddd; padding:15px; border-radius:10px; background-color:#f9f9f9">
                    <h3 style="color:#3366cc;">{poke['name'].capitalize()}</h3>
                    <p><b>Tipo:</b> {poke['type1'].capitalize()} {'/ ' + poke['type2'].capitalize() if pd.notna(poke['type2']) else ''}</p>
                    <p><b>HP:</b> {poke['hp']} | <b>Speed:</b> {poke['speed']}</p>
                    <p><b>Ofensiva Total:</b> {poke['total_offense']}<br>
                       <b>Defensiva Total:</b> {poke['total_defense']}</p>
                    <p><b>Tier:</b> {poke['tier_label']}</p>
                </div>
            """, unsafe_allow_html=True)

