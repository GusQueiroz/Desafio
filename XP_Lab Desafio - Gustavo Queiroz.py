
# coding: utf-8

# In[363]:


import pandas as pd
import matplotlib.pyplot as plt


# In[364]:


#Realiza a leitura da tabela contida na planilha realizado do Excel
dados_realizado = pd.read_excel('dados.xlsx', sheet_name = 'realizado')


# In[365]:


dados_realizado


# In[366]:


#Realiza a leitura da tabela contida na planilha orcado do Excel
dados_orcado = pd.read_excel('dados.xlsx', sheet_name = 'orcado')


# In[367]:


dados_orcado


# In[380]:


#Realiza a inversão da tabela realizado
dados_realizado = dados_realizado.T


# In[381]:


#Reseta o index que estava desorganizado
dados_realizado.reset_index(drop=True, inplace = True)


# In[382]:


#Realiza a limpeza da linha (axis = 0) que estava com valor NaN
dados_realizado.dropna(axis=0, how = 'any', inplace = True)


# In[383]:


#Renomeia as colunas
dados_realizado.rename(columns = {0: 'mês', 1: 'Realizado'}, inplace = True)


# In[384]:


dados_realizado


# In[385]:


#Realiza o merge
saida = pd.merge(dados_realizado, dados_orcado, on = 'mês', how = 'left')


# In[386]:


saida


# In[387]:


#Adicionada uma nova coluna no DataFrame, e realiza a diferença entre os valores de orçado e de realizado
saida['diff'] = (saida['orcado'].values - saida['Realizado'].values)


# In[388]:


saida


# In[389]:


#Gera o arquivo de saída .csv, e oculta a coluna do índice
saida.to_csv('XP_Lab Desafio - Gustavo Queiroz.csv',index=False)


# In[390]:


#Código para plotar o gráfico
#Definição do eixo X e eixo Y
x = saida['mês']
y = saida['orcado']
y1 = saida['Realizado']
#Realiza o aumento do tamanho do gráfico para 18 x 10 cm
plt.rcParams['figure.figsize']=(18,10)
#Gera um gráfico de barras, sendo definido as legendas e cores
plt.bar(x,y,label='Orçado',color='blue')
plt.bar(x,y1,label='Realizado',color='green')
#Definição do título do gráfico, e o título dos eixos
plt.title('Gráfico Orçamento')
plt.xlabel('Meses')
plt.ylabel('$')
#Plota as legendas, e salva o gráfico no diretório, realizando a plotagem do mesmo
plt.legend()
plt.savefig('Gráfico Orçado X Realizado.png')

