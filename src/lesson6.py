import pandas as pd
df = pd.read_excel("../data/pokemon_data.xlsx", sheet_name = 'Pokemon_1')

# ピボットテーブルで集計
## タイプ1ごとに数値データの平均値を求める
print('タイプ1平均値')
print(df.pivot_table(index='タイプ1'))
print()

## タイプ1ごとの高さの平均値を求める
print('タイプ1[高さ]平均値')
print(df.pivot_table(index='タイプ1', values= '高さ'))
print()

## タイプ1ごとの高さ、重さの平均値を求める
print('タイプ1 高さ・重さ 平均値')
print(df.pivot_table(index='タイプ1', values=['高さ', '重さ']))
print()

## タイプ1とタイプ2ごとの高さの平均値を求める
print('タイプ1/タイプ2 高さ クロス集計表')
print(df.pivot_table(index='タイプ1', columns='タイプ2', values='高さ'))
print()
print('タイプ1/タイプ2 マルチインデックス')
print(df.pivot_table(index=['タイプ1', 'タイプ2'], values='高さ'))
print()

## タイプ1ごとの高さの最大値を求める
print('タイプ1ごとの高さ最大値')
print(df.pivot_table(index='タイプ1', values='高さ', aggfunc='max'))
print()

## タイプ1ごとの高さの平均を「総計あり」で表示
print('タイプ1 高さ平均 総計あり')
print(df.pivot_table(index='タイプ1', values='高さ', aggfunc='mean', margins=True))
print()
