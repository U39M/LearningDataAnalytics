import pandas as pd
df = pd.read_excel("../data/pokemon_data.xlsx", sheet_name = 'Pokemon_1')

# 要素ごとの出現回数を集計する
## タイプ1の要素ごとに出現回数を抽出
print("タイプ1 出現回数")
print(df["タイプ1"].value_counts())
print()

## タイプ1の出現回数のデータをDataFrameに格納
print("タイプ1の出現回数のデータをDataFrameに格納")
print(pd.DataFrame(df["タイプ1"].value_counts()))
print()

print("----------------------------------------------")
print('df["タイプ1"].value_counts()')
print(type(df["タイプ1"].value_counts()))
print("----------------------------------------------")
print('pd.DataFrame(df["タイプ1"].value_counts())')
print(type(pd.DataFrame(df["タイプ1"].value_counts())))
print("----------------------------------------------")

# 要素ごとに集計する
## タイプ1ごとに数値データの平均値を求める
print("タイプ1ごとの平均値")
print(df.groupby('タイプ1').mean())
print()

# 並び替え
## 高さが昇順になるように並び替え
print("昇順ソート")
print(df.sort_values('高さ'))
print()

## 高さが降順になるように並び替え
print("降順ソート")
print(df.sort_values('高さ', ascending=False))
print()

# クロス集計表の作成
## タイプ1とタイプ2の出現回数
print("クロス集計表")
print(pd.crosstab(df["タイプ1"],df["タイプ2"]))
print()
