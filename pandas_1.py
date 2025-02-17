import pandas as pd

# Carregando o dataset corretamente que utiliza o separador ";"
data = pd.read_csv('D:\GitHub\EstudoPandas\.venv\dataset\GasPricesinBrazil_2004-2019.csv', sep=';')

# # Verificar tipo, colunas e se obtem valor Null
# print(data.dtypes,
#       data.head(),
#       data.isnull().sum())

# # Corrigido para acessar corretamente as dimensões
# print(f'O Dataframe possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/variáveis/atributos')


personagens_df = pd.DataFrame({
    'nome':['Luke SkyWalker','Yoda','Palpatine'],
    'idade':['16','1000','70'],
    'peso':['70','15','60'],
    'eh jedi':[True,True,False] #O nome da coluna pode ter espaço
})

# print(personagens_df.info())

# Renoemando as colunas
presonagens_df_renomeado = personagens_df.rename(columns={'nome':'Nome Completo','idade':'Idade'})

# Renomear direto no dataframe
personagens_df.rename(columns={
    'nome':'Nome Completo',
    'idade':'Idade'},inplace=True)



personagens_df.columns = ['NOME','IDADE','PESO','EH_JEDI']

# SERIES
# selecioando uma coluna inteira

# print(data.ESTADO) # Não é recomendado


# print(data['ESTADO'])

# print(type(data['ESTADO']))

# print(data.iloc[1]) # Acessando a segunda linha


# print(pd.Series([5.5,6.0,9.5],index=['Prova1','Prova2','Projeto'],name='Notas'))

# Quanto utiliza a cosntante, somente é um view do dataframe.
produto_view = (data['PRODUTO']) 

# Cópia do dataframe
produto_copy_bkp=data['PRODUTO'].copy()

# Atribuindo o valor constante 'Combustivel' a todos os registros da coluna 'PRODUTO'
# data['PRODUTO'] = 'Combustivel'

nrows, ncols = data.shape


novos_produtos = [ f'Produto {i}' for i in range(nrows)]

# A Quantidade de elementos da lista deve ser igual ao número de linhas do dataframe
data['PRODUTO'] = novos_produtos

data['PRODUTO']= produto_copy_bkp

# Criando uma coluna a partir de um valor constante/default
data['Coluna sem Nocao'] = 'DEFAULT'

# Criando uma coluina a partir de uma lista
data['Coluna a Partir de Lista'] =  range(data.shape[0])

# # Não funciona, devido a quantidade linhas do dataframe
# data['Não Funcionana'] = [1,2,3]

data['PREÇO MÉDIO REVENDA (dólares)'] = data['PREÇO MÉDIO REVENDA'] * 6.0

print(data)




