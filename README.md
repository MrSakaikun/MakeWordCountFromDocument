# make_word_count_from_document

1文書（document）の中にある名詞をカウントして保存するプログラムです．


## 動作環境

### 確認した動作環境
* Python 3.6.9 (anaconda3-5.0.0)

### 使用したパッケージ
* MeCab
* collections
* pickle
* csv
* os

MeCab 以外は標準で入っているパッケージのはずです．MeCabのインストールの仕方は以下のページなどを参照してください．（インターネット検索をかけたほうが早いかもしれません）

公式サイト：

https://taku910.github.io/mecab/

【これ1本でOK】MeCabをインストールしてPythonで形態素解析する方法【Mac】：

https://tech-diary.net/how-to-install-mecab/


## 使い方
0. （必要な人は）MeCabをインストールし，Pythonから使える状態にする．

1. このレポジトリをクローンする
```bash
git clone https://github.com/MrSakaikun/MakeWordCountFromDocument.git
cd MakeWordCountFromDocument
```

2. DataSetフォルダとSaveFileフォルダを作成
```bash
mkdir DataSet
mkdir SaveFile
```

3. DataSetフォルダ内に名詞をカウントしたい文書(document)のテキストファイルをコピー
```bash
cp カウントしたいファイル  ./DataSet/document.txt
```

4. 以下のコマンドを実行
```bash
python save_word_count_from_document.py
```

5. SaveFileフォルダ内にword_count.csvという名詞をカウントした結果が入っているファイルができているはずです．


## 他の使い方
* binaryfile形式で保存したい場合

save_word_count_from_document.py の最終行の関数の引数を
```
'csv'→'binaryfile'
```
に変更してください.

* 読み込む文書のファイル名の指定，保存するファイル名の変更

読み込む文書のファイル名は，save_word_count_from_document.py内にある変数を以下のように変えてください．
```python
#読み込むドキュメントファイルのPathとファイル名指定
readFilePath = '指定したいPath,ファイル名'
```
保存するファイル名も同様です．ただしファイルのフォーマットを抜いた状態で指定するよう注意してください．
```python
#保存先のPathとファイル名指定（注：フォーマットは指定しない）
saveFileName = '指定したいPath,ファイル名'
#例
saveFileName = './SaveFile/word_count.' #.まで入れる
```

* MeCab の辞書を個別で指定する場合

extract_noun.py内にある以下のコード
```python
#MeCab
m = MeCab.Tagger ()
```
このTaggerの引数を指定してください．-d 辞書のパス と指定してください．例としては
```python
m = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
```
のような感じです．


## 保存形式について
#### csvの場合

csv形式で保存した場合は，
```csv
単語,出現回数
```
のように並んでいます．出現回数の多い順となっています．

#### binaryfileの場合

パッケージ collections の Counter クラスがそのまま入っています．使い方などは以下のページなどを参照してください．

【Python】リストの要素の数え上げ、collections.Counterの使い方:

https://qiita.com/ell/items/259388b511e24625c0d7


## プログラム作成者
Yuya Sakai

GitHub:[MrSakaikun](https://github.com/MrSakaikun)

E-Mail:
yuyasakai1002[at]gmail.com

↑[at]を@に変えてください





Copyright (c) 2020 Yuya Sakai
