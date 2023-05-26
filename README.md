## 難易度
### Medium

<br>

## ▶️ Start Up & Usage
1. 次のボタンをクリックしてCloud Shell Editorを開く

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ide.cloud.google.com/?cloudshell_git_repo=https://github.com/SocSEL-SIseminar1-2023/gpa-calculater.git&cloudshell_workspace=./&cloudshell_tutorial=README.md)

2. エディタ下部のターミナルで以下のコマンドを実行する
```sh
$ cd src
$ python3 main.py
# あなたのGPAは, ___です．
```
### Sample csv
- csv_fileディレクトリにcsvファイルを3種類用意しています
- 教育サポートシステムからダウンロードしたものでも，動くと思います

```
csv_file/
  ├ row_score.csv(フル単，欠損値なし)
  ├ score_drop.csv(落としている単位あり，欠損値なし)
  └ score_kesson.csv(単位，評点共に欠損値あり)
```

### Switch csv to use
- 利用するcsvファイルの変更方法
- src/main.py
``` py diff
 def main():
  df = read_csv.load_csv('row_score.csv') <- この行を変更
  gpa = calc.get_gpa(list(df['評価']), list(df['単位']))
  print("あなたのGPAは，" + str(gpa) + "です．")
```

```diff
- df = read_csv.load_csv('row_score.csv')
+ df = read_csv.load_csv('score_kesson.csv')
```

<br>

## GPA Calculation Method
GPAの計算方法 [要項](https://www.wakayama-u.ac.jp/_files/00172820/GPA2016.pdf)
$$SUM(((評価点)-55)*単位数/10) / SUM(単位数)$$

<br>

## 📗課題の例
- リファクタリング
- 算出されるGPAの有効数字を綺麗にする
- GPA計算過程のバグを治す