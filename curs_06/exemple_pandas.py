import pandas as pd
# print(pd.__version__)
var = {"x": 1, "y": 7, "z": 2}
# var_series = pd.Series(var)
# print(var_series)
var_2 = [1, 7, 2]
var2_series = pd.Series(var_2)
# print(var2_series)

var_series = pd.Series(var, index=['x', 'z'])
# print(var_series)

data = {
    "key1": [0, 1, 2],
    "key2": [3, 4, 5],
}
# var_3 = pd.DataFrame(data)
# print(var_3)

var_3 = pd.DataFrame(data, index=['linie A', 'linie B', 'linie C'])
# print(var_3.loc['linie A']) # imi arata datele de pe o anumita linie
# print(var_3.loc['linie A', 'key2']) # imi arata datele dintr-o celula
# print(var_3.loc['linie B': 'linie C']) # slice ca sa vedem anumite intervale
# print(var_3.loc[['linie A', 'linie C'], 'key2'])


taskuri = {
    'zile': [2, 4, 5],
    'durata': [50, 40, 45]
}

var_df = pd.DataFrame(taskuri)
print(var_df)

# taskuri['zile'][1] = 100
# print(taskuri)

# var_df['zile'].loc[1] = 100
var_df.loc[1, 'zile'] = 100
print(var_df)