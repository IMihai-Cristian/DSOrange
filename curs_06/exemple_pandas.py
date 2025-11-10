import pandas as pd
# print(pd.__version__)
# var = {"x": 1, "y": 7, "z": 2}
# var_series = pd.Series(var)
# print(var_series)
# var_2 = [1, 7, 2]
# var2_series = pd.Series(var_2)
# print(var2_series)

# var_series = pd.Series(var, index=['x', 'z'])
# print(var_series)

# data = {
#     "key1": [0, 1, 2],
#     "key2": [3, 4, 5],
# }
# var_3 = pd.DataFrame(data)
# print(var_3)

# var_3 = pd.DataFrame(data, index=['linie A', 'linie B', 'linie C'])
# print(var_3.loc['linie A']) # imi arata datele de pe o anumita linie
# print(var_3.loc['linie A', 'key2']) # imi arata datele dintr-o celula
# print(var_3.loc['linie B': 'linie C']) # slice ca sa vedem anumite intervale
# print(var_3.loc[['linie A', 'linie C'], 'key2'])


# taskuri = {
#     'zile': [2, 4, 5],
#     'durata': [50, 40, 45]
# }

# var_df = pd.DataFrame(taskuri)
# print(var_df)

# taskuri['zile'][1] = 100
# print(taskuri)

# var_df['zile'].loc[1] = 100
# var_df.loc[1, 'zile'] = 100
# print(var_df)

# df = pd.read_excel('Exchange_rate.xlsx')
# print(df)
# # print(df.iloc[0])
# for x in df.index:
#     # print(df.loc[x, 'Max'])
#     if float(df.loc[x, 'Max']) <= 1.17:
#         df.drop(x, inplace=True)
# print(df)
# df.to_excel('Tabel_procesat.xlsx', index=False)

"""Matrice corelatie"""
# df = pd.DataFrame({
#     'Varsta': [20, 25, 30, 35, 40],
#     'Venit': [2000, 2500, 3000, 4000, 5000],
#     'Ore_munca': [40, 42, 38, 45, 50]
# })
#
# print(df.corr())

"""Descrierea tabelului"""
# df = pd.read_excel("Exchange_rate.xlsx")
# print(df.describe())


"""Alte atribute"""
# df = pd.read_excel("Currency.xlsx")
# print(df)
# df.dropna(inplace=True)
# print(df)
# df.fillna(0, inplace=True)
# print(df)
# df['Dec'].fillna(0, inplace=True)
# print(df)
# df.loc[7, 'Dec'] = 5555
# print(df)
# df.replace("Romanian Leu", "Romanian Ron", inplace=True)
# print(df)
# print(df.transpose())
# df.transpose().to_excel('test.xlsx')

"""PIVOT"""
# df = pd.DataFrame({
#     'Luna': ['Ian', 'Ian', 'Feb', 'Feb'],
#     'Produse': ['Telefon', 'Laptop', 'Telefon', 'Laptop'],
#     'Cost': [1000, 1500, 1400, 1800]
# })

# print(df)
# print(pivot_df)

""" PIVOT TABLE """
df = pd.DataFrame({
    'Luna': ['Ian', 'Ian', 'Ian', 'Feb', 'Feb', 'Feb'],
    'Produse': ['Telefon', 'Telefon', 'Laptop', 'Telefon', 'Laptop', 'Laptop'],
    'Cost': [1000, 1500, 1400, 1800, 1600, 1900]
})

# pivot_table = pd.pivot_table(df, index='Luna', columns='Produse', values='Cost', aggfunc='sum')
# print(pivot_table)
# pivot_table = pd.pivot_table(df, index='Luna', columns='Produse', values='Cost', aggfunc='mean')
# print(pivot_table)
# pivot_table = pd.pivot_table(df, index='Luna', columns='Produse', values='Cost', aggfunc='count')
# print(pivot_table)
pivot_table = pd.pivot_table(df, index='Luna', columns='Produse', values='Cost', aggfunc='sum', margins=True)
print(pivot_table)
