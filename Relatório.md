#  Análise de Potencial Competitivo dos Pokémon da Região de Kanto

##  Introdução

A proposta deste projeto é auxiliar uma empresa de jogos na criação de um novo modo competitivo de batalhas entre Pokémon da região de Kanto. O foco está em identificar os Pokémon com maior potencial ofensivo e defensivo, agrupando-os em faixas chamadas de *Tiers*, com o objetivo de balancear os combates de forma justa.

##  Dataset Utilizado

O dataset contém os 150 Pokémon da região de Kanto e apresenta as seguintes colunas principais:

- `pokedex_no`: Número da Pokédex
- `name`: Nome do Pokémon
- `type1` / `type2`: Tipos elementares
- `hp`: Pontos de vida
- `attack`, `defense`: Atributos físicos
- `special-attack`, `special-defense`: Atributos especiais
- `speed`: Velocidade
- `moves`: Lista de golpes disponíveis

Esses dados foram utilizados para compor uma análise exploratória e uma clusterização para definição dos Tiers.

##  Objetivo

> Identificar os Pokémon mais fortes ofensiva ou defensivamente para classificá-los em Tiers e auxiliar na criação de um sistema balanceado de batalhas competitivas.

##  Metodologia

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

###  Gráfico de Dispersão dos Tiers

*Exemplo de visualização que ilustra os clusters (tiers) no espaço ofensivo-defensivo:*

![Gráfico de Tiers](exemplo_dispersao.png)

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

##  Conclusão

A metodologia de clusterização se mostrou eficaz para separar os Pokémon em grupos distintos com base em seu poder bruto. Esse tipo de classificação é útil para balancear torneios, restringindo o uso de Pokémon mais fortes e garantindo batalhas mais justas.

Esse modelo pode ser adaptado no futuro incluindo mais variáveis, como habilidades especiais, vantagens de tipo ou até dados de vitórias em batalhas reais.

---

##  Tecnologias utilizadas

- Python 3
- Pandas
- Scikit-learn
- Streamlit
- VS Code

