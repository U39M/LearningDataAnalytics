import pandas as pd

# Excelのデータを読み込む
# 読み込んだデータを変数に格納
df = pd.read_excel("../data/pokemon_data.xlsx")

# Sheet名を指定してデータを読み込む
pd.read_excel("../data/pokemon_data.xlsx", sheet_name= 'Pokemon_1')

# 変数の最初の5行を出力させる
print("==============")
print("最初5行")
print(df.head())
print("==============")

# 変数の最初の3行を出力させる
print("==============")
print("最初3行")
print(df.head(3))
print("==============")

# 変数の最後の5行を表示させる
print("==============")
print("最後5行")
print(df.tail())
print("==============")

# 変数からデータをランダムに3行表示させる
print("==============")
print("ランダム3行")
print(df.sample(3))
print("==============")

