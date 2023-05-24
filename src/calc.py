import pandas as pd

#gpaを計算する関数の定義
def get_gpa(score_list: list, credit_list: list):

  # 引数の配列の中身をint方に変換
  score_list, credit_list = convert2int(score_list, credit_list)
  
  # GP積の和を求める
  result = 0
  for i, j in zip(score_list, credit_list):
  
    if j == 2: # 2単位の授業の場合
      gpa_tmp = (i-55)*(2/10)
      result += gpa_tmp
    else:
      gpa_tmp = (i-55)/10
      result += gpa_tmp

  # GPAを求める
  result = result / sum(credit_list)

  return result


def convert2int(score_list: list, credit_list: list):
  # 保存しておくためのリストを初期化
  score_list_int = []
  credit_list_int = []

  # int方に変換したものを格納
  for i in score_list:
    if not pd.isna(i):
      score_list_int.append(int(i))
    else:
      score_list_int.append(0)

  for i in credit_list:
    if not pd.isna(i):
      credit_list_int.append(int(i))
    else:
      credit_list_int.append(0)

  return score_list_int, credit_list_int
