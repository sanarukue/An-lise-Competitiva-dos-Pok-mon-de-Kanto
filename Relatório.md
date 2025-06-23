#  Análise de Potencial Competitivo dos Pokémon da Região de Kanto

##  Tema do Proeto

A proposta deste projeto é auxiliar uma empresa de jogos na criação de um novo modo competitivo de batalhas entre Pokémon da região de Kanto. O foco está em identificar os Pokémon com maior potencial ofensivo e defensivo, agrupando-os em faixas chamadas de *Tiers*, com o objetivo de balancear os combates de forma justa.

## URL do Projeto no GitHub

[https://github.com/sanarukue/An-lise-Competitiva-dos-Pok-mon-de-Kanto](https://github.com/sanarukue/An-lise-Competitiva-dos-Pok-mon-de-Kanto)

##  Dataset Utilizado

O dataset contém os 150 Pokémon da região de Kanto e apresenta as seguintes colunas principais:
## Principais Variáveis

- `pokedex_no`: Número da Pokédex
- `name`: Nome do Pokémon
- `type1` / `type2`: Tipos elementares
- `hp`: Pontos de vida
- `attack`, `defense`: Atributos físicos
- `special-attack`, `special-defense`: Atributos especiais
- `speed`: Velocidade
- `moves`: Lista de golpes disponíveis

Esses dados foram utilizados para compor uma análise exploratória e uma clusterização para definição dos Tiers.

## Origem
O dataset utilizado é baseado nas estatísticas oficiais dos Pokémon da primeira geração (Kanto), com informações extraídas de fontes como o site [Kaggle](https://www.kaggle.com/datasets/atharvarghadigaonkar/kanto-pokemon-dataset-with-all-moves).


##  Objetivo

> Identificar os Pokémon mais fortes ofensiva ou defensivamente para classificá-los em Tiers e auxiliar na criação de um sistema balanceado de batalhas competitivas.

## Transformações Realizadas

Utilizamos Python com bibliotecas como `pandas`, `scikit-learn`, `matplotlib` e `streamlit`. As principais etapas foram:

- Cálculo de métricas agregadas:
  - **total_offense** = attack + special-attack
  - **total_defense** = defense + special-defense
- Análise de distribuição de atributos
- Clusterização com **KMeans (k=4)** usando as variáveis:  
  `total_offense`, `total_defense`, `hp` e `speed`
- Geração de visualizações interativas com Streamlit

##  Clusterização e Tiers

O algoritmo KMeans foi utilizado para agrupar os Pokémon em 4 faixas distintas de poder. Os grupos foram ordenados com base no valor médio ofensivo/defensivo de seus membros e nomeados como:

- **Tier 1 (Mais Forte)**
- **Tier 2**
- **Tier 3**
- **Tier 4 (Mais Fraco)**

A clusterização leva em conta o potencial bruto de cada Pokémon (ataque, defesa, vida e velocidade), desconsiderando temporariamente elementos como moveset ou sinergia de tipos.

##  Resultados

# Modelos Utilizados ou Desenvolvidos

- **Algoritmo de Clusterização:**
  - `KMeans` da biblioteca `scikit-learn`
  - Definimos 4 clusters (tiers) de forma não supervisionada, com base nas características de batalha dos Pokémon.

- **Visualizações Interativas:**
  - Utilização da biblioteca `Streamlit` para criar um dashboard interativo.
  - Gráficos de dispersão, tabelas interativas e filtros por tipo de Pokémon.

- **Visualizações Gráficas:**
  - Gráficos de barras para distribuição por Tier.
  - Gráficos de dispersão com cores por Tier.

###  Distribuição de Pokémon por Tier

*Gráfico de barras com a quantidade de Pokémon em cada tier.*

###  Cards por Pokémon

Cada Pokémon pode ser visualizado individualmente em cards contendo:
- Nome
- Tipo(s)
- HP
- Speed
- Total Ofensivo e Defensivo
- Tier atribuído

O projeto resultou na categorização dos Pokémon de Kanto em 4 níveis competitivos (Tier 1 até Tier 4), baseados no balanceamento entre ataque, defesa, HP e velocidade.

- **Tier 1:** Pokémon com alto poder ofensivo e/ou defensivo (ex.: Mewtwo, Dragonite).
- **Tier 2:** Pokémon fortes, mas com alguma fraqueza evidente.
- **Tier 3:** Pokémon medianos e equilibrados.
- **Tier 4:** Pokémon com menor potencial competitivo

##  Conclusão

A metodologia de clusterização se mostrou eficaz para separar os Pokémon em grupos distintos com base em seu poder bruto. Esse tipo de classificação é útil para balancear torneios, restringindo o uso de Pokémon mais fortes e garantindo batalhas mais justas.

Esse modelo pode ser adaptado no futuro incluindo mais variáveis, como habilidades especiais, vantagens de tipo ou até dados de vitórias em batalhas reais.

---

## Tecnologias Utilizadas
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- VS Code

## Referências

- https://www.kaggle.com/abcsds/pokemon
- https://streamlit.io/
- https://pandas.pydata.org/
- https://scikit-learn.org