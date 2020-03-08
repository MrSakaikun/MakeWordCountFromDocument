from make_word_count_from_document import make_wordcount_from_document_txt
import pickle
import csv
import os


#読み込むドキュメントファイルのPathとファイル名指定
readFilePath = './DataSet/document.txt'

#保存先のPathとファイル名指定（注：フォーマットは指定しない）
saveFileName = './SaveFile/word_count.'


def save_wordcount_from_document_txt(format='binaryfile'):

    saveFilePath = saveFileName + format

    #ファイルが存在する場合は上書きするかどうか確認
    if os.path.isfile(saveFilePath):
        print(saveFilePath+"は存在しています．再作成しますか？再作成する場合はcを，それ以外はqを入力してください")
        if not "c" == input():
            return

    #documentを読み込んでwordcountする
    wordCounter = make_wordcount_from_document_txt(filePath=readFilePath)

    #保存形式がcsvの時
    if format == 'csv':

        print("making and sorting wordList.")
        #リスト型に変換し出現頻度順に並べ替え
        wordList = list(wordCounter.items())
        wordList.sort(key=lambda x:x[1],reverse=True)

        #csv形式で書き込み
        print("saving :"+saveFilePath)
        with open(saveFilePath,'w') as f:
            writer = csv.writer(f)
            for word in wordList:
                writer.writerow(word)

    #保存形式がbinaryfileの時
    if format == 'binaryfile':
        print("saving :"+saveFilePath)
        with open(saveFilePath,'wb') as f:
            pickle.dump(wordCounter,f)



if __name__ == '__main__':
    save_wordcount_from_document_txt(format='csv')
