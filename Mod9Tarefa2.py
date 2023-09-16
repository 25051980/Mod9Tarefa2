#!/usr/bin/env python
# coding: utf-8

# # Livro para consulta:
# - https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html
# - https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html
#     

# # 1. Importando bibliotecas <a name="import"></a>
# 
# <div style="text-align: right"
#      
# [Voltar ao índice](#Contents)

# In[8]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# # 2. Carregando o dataframe SINASC <a name="read"></a>
# <div style="text-align: right"
#      
# [Voltar ao índice](#Contents)

# In[9]:


sinasc_raw = pd.read_csv('SINASC_RO_2019.csv')
sinasc_raw.head()


# # Tarefa 2

# ### 1. Crie 2 faixas de Latitude do município (munResLat) sendo uma acima e outra abaixo de -10.5 e aplique o groupby usando essas faixas como chave e realize operações de soma, media, minimo, maximo, mediana, desvio padrao, variancia pra pelo menos 2 variáveis numéricas ainda não utilizadas

# In[25]:


import pandas as pd

# Leitura do arquivo CSV
sinasc_raw = pd.read_csv('SINASC_RO_2019.csv')

# Crie duas faixas de Latitude
sinasc_raw['Faixa_Latitude'] = pd.cut(sinasc_raw['munResLat'], bins=[-float('inf'), -10.5, float('inf')],
                                      labels=['Abaixo de -10.5', 'Acima de -10.5'])

# Suponha que você tenha outras variáveis numéricas no DataFrame
var1 = 'munResLat'
var2 = 'munResLat'

agg_operations = {
    var1: ['sum', 'mean', 'min', 'max', 'median', 'std', 'var'],
    var2: ['sum', 'mean', 'min', 'max', 'median', 'std', 'var']
}

summary = sinasc_raw.groupby('Faixa_Latitude').agg(agg_operations)

# Imprima o resultado
print(summary)



# ### 2. Crie 2 faixas da área dos municípios (munResArea) sendo uma acima e outra abaixo de 3000 e aplique o groupby usando essas faixas como chave e realize operações de soma, media, minimo, maximo, mediana, desvio padrao, variancia pra pelo menos 2 variáveis numéricas ainda não utilizadas
# 

# In[26]:


import pandas as pd

# Leitura do arquivo CSV
sinasc_raw = pd.read_csv('SINASC_RO_2019.csv')

# Crie duas faixas de Latitude
sinasc_raw['Faixa_Latitude'] = pd.cut(sinasc_raw['munResLat'], bins=[-float('inf'), -10.5, float('inf')],
                                      labels=['Abaixo de -10.5', 'Acima de -10.5'])

# Suponha que 'munResArea' é uma variável numérica não utilizada
var1 = 'munResArea'
var2 = 'munResArea'

agg_operations = {
    var1: ['sum', 'mean', 'min', 'max', 'median', 'std', 'var'],
    var2: ['sum', 'mean', 'min', 'max', 'median', 'std', 'var']
}

summary = sinasc_raw.groupby('Faixa_Latitude').agg(agg_operations)

# Imprima o resultado
print(summary)


# ### 3. Determine faixas na variável munResAlt e aplique o groupby usando essas faixas como chave e realize operações de soma, media, minimo, maximo, mediana, desvio padrao, variancia pra pelo menos 2 variáveis numéricas ainda não utilizadas

# In[27]:


import pandas as pd

# Leitura do arquivo CSV
sinasc_raw = pd.read_csv('SINASC_RO_2019.csv')

# Crie faixas na variável 'munResAlt'. Por exemplo, você pode criar 3 faixas:
bins = [0, 500, 1000, 1500, 2000]  # Defina as faixas conforme necessário
labels = ['Faixa1', 'Faixa2', 'Faixa3', 'Faixa4']

sinasc_raw['Faixa_munResAlt'] = pd.cut(sinasc_raw['munResAlt'], bins=bins, labels=labels)

# Suponha que 'Variavel1' e 'Variavel2' são variáveis numéricas não utilizadas
var1 = 'munResAlt'
var2 = 'munResAlt'

agg_operations = {
    var1: ['sum', 'mean', 'min', 'max', 'median', 'std', 'var'],
    var2: ['sum', 'mean', 'min', 'max', 'median', 'std', 'var']
}

summary = sinasc_raw.groupby('Faixa_munResAlt').agg(agg_operations)

# Imprima o resultado
print(summary)


# ### 4. Plote no mesmo grafico ao longo do tempo a idade media das mulheres de cada regiao imediatas de rondonia
# https://pt.wikipedia.org/wiki/Lista_de_regi%C3%B5es_geogr%C3%A1ficas_intermedi%C3%A1rias_e_imediatas_de_Rond%C3%B4nia

# In[48]:


import pandas as pd

# Ler o DataFrame a partir do arquivo ou usar o DataFrame existente
# df = pd.read_csv("seuarquivo.csv")

# Calcular a idade média das mulheres
idade_media = df['IDADEMAE'].mean()

print(f"A idade média das mulheres é: {idade_media:.2f} anos")




# In[49]:


idade_media_por_regiao = df.groupby('munResNome')['IDADEMAE'].mean()
print(idade_media_por_regiao)


# In[51]:


import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv("SINASC_RO_2019.csv")

# Calcular a idade média total das mulheres
idade_media_total = df['IDADEMAE'].mean()

# Criar um DataFrame com a idade média por região
idade_media_por_regiao = df.groupby('munResNome')['IDADEMAE'].mean().reset_index()

# Plotar a idade média por região e a idade média total no mesmo gráfico
plt.figure(figsize=(12, 6))
plt.plot(idade_media_por_regiao['munResNome'], idade_media_por_regiao['IDADEMAE'], marker='o', label='Idade Média por Região')
plt.axhline(idade_media_total, color='red', linestyle='--', label='Idade Média Total', linewidth=2)
plt.title('Idade Média das Mulheres por Região Imediata em Rondônia')
plt.xlabel('Região Imediata')
plt.ylabel('Idade Média')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ### 5. Utilize a tabela do link abaixo e crie faixas utilizando o mapping e gere agrupamentos utilizando essas faixas como chave
# 

# ### 5.1 IDH
# A - https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Rond%C3%B4nia_por_IDH-M
# 

# In[53]:


import pandas as pd

# Ler os dados do IDH municipal (você pode adaptar isso ao seu DataFrame)
data = {
    'Município': [
        'Alta Floresta d\'Oeste',
        'Alto Alegre dos Parecis',
        'Alto Paraíso',
        # Adicione mais municípios conforme necessário
    ],
    'IDH municipal': [
        0.641,
        0.592,
        0.625,
        # Adicione mais valores de IDH correspondentes aos municípios
    ]
}

df_idh = pd.DataFrame(data)

# Definir as faixas e os valores correspondentes
faixas = {
    'Baixo': (0, 0.5),
    'Médio': (0.5, 0.7),
    'Alto': (0.7, 0.8),
    'Muito Alto': (0.8, 1.0)
}

# Criar uma função para mapear os valores de IDH para faixas
def mapear_faixa(idh):
    for faixa, (min_valor, max_valor) in faixas.items():
        if min_valor <= idh < max_valor:
            return faixa
    return 'Desconhecido'

# Aplicar a função de mapeamento para criar uma nova coluna de faixas
df_idh['Faixa IDH'] = df_idh['IDH municipal'].apply(mapear_faixa)

# Agrupar os dados por faixa de IDH
grupo_idh = df_idh.groupby('Faixa IDH')

# Visualizar os grupos e estatísticas de cada grupo
for faixa, grupo in grupo_idh:
    print(f"Faixa de IDH: {faixa}")
    print(grupo)
    print()


# Os municípios de Porto Velho, Vilhena, Cacoal, Ji-Paraná e Pimenta Bueno possuem um IDH-M (Índice de Desenvolvimento Humano Municipal) classificado como "Alto" em 2010.
# 
# A cidade de Porto Velho se destaca com o IDH municipal mais alto entre esses municípios em 2010, o que indica um melhor desenvolvimento em termos de renda, longevidade e educação.
# 
# Os municípios com IDH-M classificado como "Médio" incluem Cerejeiras, Jaru, Colorado do Oeste, Ouro Preto do Oeste, Espigão d'Oeste, Santa Luzia d'Oeste, Pimenteiras do Oeste, Presidente Médici, Castanheiras e Guajará-Mirim, entre outros.
# 
# Também podemos observar municípios com IDH-M classificado como "Baixo" e "Muito Baixo", mas parece que não há municípios com IDH-M "Muito Alto".
# 
# Não foi fornecida a informação sobre a idade mediana das mulheres que deram à luz em cada um desses municípios. Portanto, não podemos tirar conclusões sobre essa variável com base nos dados apresentados.
# 
# 

# ### 5.2 IFDM 
# B - https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Rond%C3%B4nia_por_IFDM
# 

# In[55]:


import pandas as pd

# Criar um dicionário com os dados
data = {
    'Posição': [1, 2, 3, 4, 5],
    'Município': ['Ariquemes', 'Vilhena', 'Pimenta Bueno', 'Porto Velho', 'Ji-Paraná'],
    'IFDM': [0.7746, 0.7465, 0.7383, 0.7257, 0.7117],
    'Categoria': ['Desenvolvimento Moderado', 'Desenvolvimento Moderado', 'Desenvolvimento Moderado', 'Desenvolvimento Moderado', 'Desenvolvimento Moderado']
}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Exibir o DataFrame
print(df)


# In[56]:


import pandas as pd

# Suponha que você tenha um DataFrame chamado 'df' com as colunas 'Município' e 'IFDM'

# Definir as faixas de IFDM
faixas_ifdm = {
    'Desenvolvimento Alto': (0.7, 1.0),
    'Desenvolvimento Moderado': (0.5, 0.7),
    'Desenvolvimento Regular': (0.4, 0.5),
    'Desenvolvimento Baixo': (0.0, 0.4)
}

# Criar uma função para mapear os valores IFDM para faixas
def mapear_faixa_ifdm(ifdm):
    for faixa, (min_valor, max_valor) in faixas_ifdm.items():
        if min_valor <= ifdm <= max_valor:
            return faixa
    return 'Desconhecido'

# Aplicar a função de mapeamento para criar uma nova coluna de faixas IFDM
df['Faixa IFDM'] = df['IFDM'].apply(mapear_faixa_ifdm)

# Agrupar os municípios com base nas faixas IFDM
grupo_ifdm = df.groupby('Faixa IFDM')

# Visualizar os grupos e os municípios em cada grupo
for faixa, grupo in grupo_ifdm:
    print(f"Faixa de IFDM: {faixa}")
    print(grupo['Município'])
    print()


# Diferença no Desenvolvimento: Os municípios de Rondônia apresentam uma ampla variação em termos de desenvolvimento, com alguns deles classificados como "Desenvolvimento Moderado", enquanto outros estão na categoria "Desenvolvimento Regular". Não há municípios na categoria "Desenvolvimento Alto" ou "Desenvolvimento Baixo" com base nesses dados.
# 
# Principais Municípios: Ariquemes, Vilhena, Pimenta Bueno, Porto Velho, Ji-Paraná e Cacoal são os municípios que lideram em termos de desenvolvimento moderado, com índices IFDM mais altos. Isso sugere que essas áreas podem oferecer melhores condições de vida, educação, emprego e saúde em comparação com outros municípios.
# 
# Desenvolvimento Regular: Os municípios classificados como "Desenvolvimento Regular" estão distribuídos em todo o estado. Isso indica que, embora essas áreas possam não estar no topo em termos de desenvolvimento, elas ainda têm um nível aceitável de qualidade de vida e infraestrutura.
# 
# Áreas de Melhoria: Os municípios com índices IFDM mais baixos podem considerar identificar áreas de melhoria em termos de educação, renda e longevidade para elevar seu índice de desenvolvimento no futuro.
# 
# Avaliação Contínua: É importante ressaltar que esses índices são de 2013 e podem ter mudado ao longo dos anos. Portanto, uma avaliação contínua e investimentos em áreas-chave são essenciais para melhorar o desenvolvimento humano em todos os municípios de Rondônia.

# ### 5.3 PIB
# C - https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Rond%C3%B4nia_por_PIB
# 

# In[57]:


import pandas as pd

# Defina os dados em uma lista de dicionários
dados = [
    {"Município": "Porto Velho", "PIB": 17912070},
    {"Município": "Ji-Paraná", "PIB": 3783972},
    {"Município": "Vilhena", "PIB": 2831175},
    {"Município": "Ariquemes", "PIB": 2579830},
    {"Município": "Cacoal", "PIB": 2261644},
    # Continue com os outros municípios...
]

# Crie um DataFrame a partir dos dados
df_pib = pd.DataFrame(dados)

# Visualize o DataFrame
print(df_pib)


# In[62]:


import pandas as pd
import matplotlib.pyplot as plt

# Dados dos municípios e seus PIBs
dados = [
    {"Município": "Porto Velho", "PIB": 17912070},
    {"Município": "Ji-Paraná", "PIB": 3783972},
    {"Município": "Vilhena", "PIB": 2831175},
    # ... (restante dos dados)
]

# Criação do DataFrame
df = pd.DataFrame(dados)

# Definindo as faixas de PIB
faixas = [
    {"Faixa": "Acima de 1 Bilhão", "Limite Inferior": 1000000000, "Limite Superior": float("inf")},
    {"Faixa": "Acima de 500 Milhões", "Limite Inferior": 500000000, "Limite Superior": 1000000000},
    {"Faixa": "Acima de 300 Milhões", "Limite Inferior": 300000000, "Limite Superior": 500000000},
    {"Faixa": "Acima de 200 Milhões", "Limite Inferior": 200000000, "Limite Superior": 300000000},
    {"Faixa": "Acima de 100 Milhões", "Limite Inferior": 100000000, "Limite Superior": 200000000},
    {"Faixa": "Até 100 Milhões", "Limite Inferior": 0, "Limite Superior": 100000000},
]

# Função para atribuir uma faixa a cada município
def atribuir_faixa(pib):
    for faixa in faixas:
        if faixa["Limite Inferior"] <= pib < faixa["Limite Superior"]:
            return faixa["Faixa"]
    return "Faixa não encontrada"

# Aplica a função para criar uma nova coluna "Faixa de PIB"
df["Faixa de PIB"] = df["PIB"].apply(atribuir_faixa)

# Contagem de municípios em cada faixa
contagem_faixas = df["Faixa de PIB"].value_counts().sort_index()

# Criação do gráfico de barras
plt.figure(figsize=(10, 6))
contagem_faixas.plot(kind="bar", color="skyblue")
plt.title("Número de Municípios por Faixa de PIB")
plt.xlabel("Faixa de PIB")
plt.ylabel("Número de Municípios")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Concentração Econômica: Porto Velho, Ji-Paraná e Vilhena são as cidades com os maiores PIBs em Rondônia. Porto Velho se destaca ainda mais, sendo a cidade com o maior PIB do estado e o terceiro maior da região Norte do Brasil.
# 
# Municípios de Destaque: Além das três principais cidades, Ariquemes e Cacoal também têm PIBs significativos, ocupando a 4ª e 5ª posições, respectivamente.
# 
# Variação de PIB: Os dados também mostram que, ao longo dos anos, muitos municípios aumentaram seus PIBs. Isso indica um crescimento econômico em várias áreas de Rondônia.
# 
# Distribuição Geográfica: Municípios com PIBs mais altos estão distribuídos em diferentes partes do estado, sugerindo uma distribuição mais equilibrada da atividade econômica.
# 
# Variação nas Mudanças: Alguns municípios experimentaram um aumento significativo em seus PIBs, enquanto outros tiveram mudanças mínimas ou mesmo baixas. Isso pode refletir diferenças nas atividades econômicas locais e no investimento em desenvolvimento.
# 
# Importância do Setor Primário: Dentre os municípios que tiveram um aumento notável, muitos estão relacionados à agricultura e pecuária, indicando a importância do setor primário na economia de Rondônia.
# 
# Desafios para Municípios Menores: Municípios com PIBs menores enfrentam desafios econômicos, o que pode impactar o desenvolvimento local. A variação de PIB nesses municípios também pode ser mais limitada.

# ### Analise as respostas encontradas, tire algum insight delas, conte pra gente algo encontrado nos dados.

# Exemplo:
# - Ah, descobri que a idade mediana das mulheres que deram a luz no ano de 2019 dos municipios com o PIB mais alto é a maior dentre todas.

# In[ ]:




