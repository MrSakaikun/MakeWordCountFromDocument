from collections import Counter
from extract_noun import extract_noun_from_text

#documentに入っている文章の名詞をカウントする
def make_wordcount_from_document_txt(filePath):
    #事前準備
    word_count = []
    wordCounter = Counter()


    print("starting to load document.")
    with open(filePath,'r') as f:
        textSize = len(f.readlines())


    with open(filePath,'r') as fr:
        i = 0
        #名詞を抽出しwordCounterにカウントした結果を追加
        for sentence in fr:
            #表示用
            i += 1
            print(str(i)+"/"+str(textSize))

            #名詞抽出と追加
            nounList = extract_noun_from_text(sentence)
            for noun in nounList:
                word_count.append(noun)

            #一定回数実行したらCounterに移す
            if i % 500000 == 0:
                wordCounter += Counter(word_count)
                word_count = []

        #残り（端数）のword_countもwordCounterに追加
        wordCounter += Counter(word_count)

    print("completed extracting noun.")

    #wordCounterを返す
    return wordCounter
