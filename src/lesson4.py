import pandas as pd
df = pd.read_excel("../data/pokemon_data.xlsx", sheet_name = 'Pokemon_1')

# データの行数を数える
print("行数")
print(len(df))
print()

# データの行数・列数を数える
print("行数・列数")
print(df.shape)
print()

# カラムごとにデータ数を数える
print("カラム別のデータ数")
print(df.count())
print()

# 高さの合計値を取り出す
print("高さ：合計値")
print(df["高さ"].sum())
print()

# 高さの平均値を取り出す
print("高さ：平均値")
print(df["高さ"].mean())
print()

# 高さの中央値を取り出す
print("高さ：中央値")
print(df["高さ"].median())
print()

# 高さの最大値を取り出す
print("高さ：最大値")
print(df["高さ"].max())
print()

# 高さの最小値を取り出す
print("高さ：最小値")
print(df["高さ"].min())
print()

# 高さの標準偏差を取り出す
print("高さ：標準偏差")
print(df["高さ"].std())
print()

# 高さの基本統計量を取得する
print("基本統計量")
print(df.describe())
print()

# 数値型以外の統計情報の取得
print("数値型以外の統計情報")
print(df.describe(include='object'))
print()

# データ型の取得
print("データ型の取得")
print(df.dtypes)
print()

# カラムごとのNullの個数を取得
print("Nullの個数")
print(df.isnull().sum())
print()

# データ型とデータが存在している個数を取得
print("データ型とデータ数")
print(df.info())
print()