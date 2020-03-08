import MeCab


#MeCab
m = MeCab.Tagger ()

#形態素解析
def mecab_parse(text):
    #引数はテキスト（文）
    #返り値はMeCabで形態素解析した結果を3次配列の形式にしたもの
    mecabFormat = []
    for txt in m.parse(text).split('\n'):
        t = txt.split('\t')
        if len(t)==2:
            xt = t[1].split(',')
            mecabFormat.append([t[0],xt])
    #形態素解析の形式で返す
    return mecabFormat

#文章から名詞を抽出
def extract_noun_from_text(text):
    #名詞を入れる場所
    nounList = []
    #形態素解析のフォーマットを取得
    mecabFormat = mecab_parse(text)
    #名詞だったら追加して返す
    for word_format in mecabFormat:
        if word_format[1][0] == '名詞':
            nounList.append(word_format[0])
    return nounList
