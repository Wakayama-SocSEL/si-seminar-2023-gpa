# ライブラリのインポート
import pandas as pd

# csvファイルをDF型で読み込む
def load_csv(name: str):
  # df = pd.read_csv('../csv_file/' + name, encoding='utf-8', header=5)
  df = pd.read_csv('../csv_file/' + name, encoding='utf-8', header=5)
  df = df.reset_index(drop=True)
  lim = list(df['科目名'] == ' ')
  df = df.loc[0:lim.index(True)-1]
  df = df[df['単位'].notnull()]
  df = df.reset_index(drop=True)

  return df
