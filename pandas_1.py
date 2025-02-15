import pandas as pd

# Carregando o dataset corretamente que utiliza o separador ";"
data = pd.read_csv('D:\GitHub\EstudoPandas\.venv\dataset\GasPricesinBrazil_2004-2019.csv', sep=';')

# Verificar tipo, colunas e se obtem valor Null
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

print(personagens_df)
