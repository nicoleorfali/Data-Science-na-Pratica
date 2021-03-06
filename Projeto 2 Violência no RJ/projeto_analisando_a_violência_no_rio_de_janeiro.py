# -*- coding: utf-8 -*-
"""Projeto Analisando a Violência no Rio de Janeiro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S4Uun-RN1PHKKvqPuj82-OyQ83c19_3U

**Instruções para o Projeto**

* Você deve importar o pandas e importar a base de dados da Polícia Militar do Rio de Janeiro sobre a violência
  * O arquivo `csv` se encontra no endereço abaixo:
    * https://raw.githubusercontent.com/carlosfab/dsnp2/master/datasets/violencia_rio.csv
  * Este arquivo `csv` foi pré-processado minimamente por mim, para focar nos pontos aprendidos neste Módulo
  * Este é o site oficial, do Governo do Estado do Rio de Janeiro:
    * http://www.ispdados.rj.gov.br/estatistica.html
  * Um *dashboard* interativo e visual pode ser encontrado no site abaixo:
    * http://www.ispvisualizacao.rj.gov.br/index.html
  * Você está livre para apagar, alterar e acrescentar o que quiser!
  * Se você sentiu dificuldade, não se preocupe! Disponibilizei a minha própria solução para servir de guia, porém tente fazer a sua por você mesmo inicialmente.
    * Se sentir perdido é normal, mas acredite: O seu cérebro vai começar a adquirir uma capacidade nova de pensar em hipóteses e questionar dados.
  
  
---

# Analisando a Violência no Rio de Janeiro

Escreva uma breve introdução contextualizando o problema e o que você vai fazer...

## Obtenção dos Dados


Descreva a fonte dos seus dados e um breve resumo sobre o que se pode esperar desse *dataset*

## Importando as bibliotecas necessárias
"""

# Commented out IPython magic to ensure Python compatibility.
#importando bibliotecas e formatando variáveis
import pandas as pd
# %precision %.2f
pd.options.display.float_format = '{:,.2f}'.format

"""### Importando os dados"""

df = pd.read_csv('https://raw.githubusercontent.com/carlosfab/dsnp2/master/datasets/violencia_rio.csv')

"""## Análise Inicial dos Dados

Breve contextualização...

Descreva e execute as seguintes etapas:

* Qual o tamanho do seu DataFrame (`shape`)
* Extrair e imprimir os nomes das colunas (`columns`)
* Quais os tipos das variáveis (`dtypes`)
* Visualizar as 5 primeiras linhas (`head`)
* Identifique a porcentagem de valores ausentes das colunas
"""

#analisando o tamanho do dataset
df.shape

#verificando o nome das colunas
df.columns

#analisando os tipos de dados armazenados no dataset
df.info()

#conhecendo as primeiras entradas do dataset
df.head()

#conhecendo o percentual de dados ausentes por coluna, em ordem decrescente
(df.isnull().sum().sort_values(ascending=False)/df.shape[0])*100

"""## Informações Estatísticas da Violência no Rio de Janeiro

Breve contextualização...

Descreva e execute as seguintes etapas:

* Imprima o resumo estatístico do seu DataFrame (`describe`)
* Encontre as médias das seguintes variáveis (colunas):
  * `roubo_veiculo`
  * `furto_veiculos`
  * `recuperacao_veiculos`
* Calcule qual a porcentagem de carros recuperados em relação aos carros roubados + carros furtados:
  * $\frac{\text{recuperacao_veiculos}}{\text{roubo_veiculo} + \text{furto_veiculos}}$
* Encontre os valores máximos (`max`) e mínimos (`min`) da coluna `hom_doloso`
"""

#conhecendo dados estatísticos do dataset
df.describe()

#conhecendo a média de roubo de veículos
df.roubo_veiculo.mean()

#conhecendo a média de 
df.furto_veiculos.mean()

#conhecendo a média de 
df.recuperacao_veiculos.mean()

#calculando o percentual de recuperação de veículos, em relação ao total furtado ou roubado
(df.recuperacao_veiculos.sum()/(df.roubo_veiculo.sum() + df.furto_veiculos.sum()))*100

#encontrando o número máximo de homicídios dolosos por mês
df.hom_doloso.max()

#encontrando o número máximo de homicídios culposos por mês
df.hom_culposo.max()

"""## Visualização de Dados

Breve contextualização...

Plote e comente os seguintes gráficos:

* Histograma de `hom_doloso`
* Gráfico de linhas para a variável `roubo_em_coletivo`
"""

#plotando histograma dos homicícios dolosos
df.hom_doloso.hist();

df.roubo_em_coletivo.plot();

"""## Conclusão

Escreva suas conclusões e análises sobre os indicadores de violência do Rio de Janeiro...
"""

