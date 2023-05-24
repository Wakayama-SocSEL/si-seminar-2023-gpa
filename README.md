## Set Up Python(pythonがインストールされていない方)
次のページからpythonのインストールを行なってください [リンク](https://www.javadrive.jp/python/install/index1.html)
インストールされているかの確認方法
```sh
$ python3 -V
# python 3.X.X のようになっていればOK
```

<br>

## Start Up & Usage(Windowsの方はPowerShellを推奨)
```sh
$ git clone https://github.com/Wakayama-SocSEL/si-seminar-2023-gpa.git
$ cd si-seminar-2023-gpa/src
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