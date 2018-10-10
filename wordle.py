from pymongo import MongoClient,ASCENDING, DESCENDING
from PIL import Image
import jieba
import re
jieba.load_userdict("newdict.txt")
import jieba.posseg as pseg
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
class wordle:
    def data(self):
        stopwords={}
        fstop = open('newdict.txt','r')
        for i in fstop:
            stopwords[i.strip()] = i.strip()
        fstop.close()
        #print (stopwords)
        #fout = open('tt.txt','w')
        a = db[table].find()
        for i in a:
            if i.get("sn")>1:
                line = (i.get("name").strip())
                wordList =list(jieba.cut(line))
                outStr=''
                for j in wordList:
                    if j not in stopwords:
                        outStr += j
                        outStr += ' '
                #db[table].update({"sn":i.get("sn")},{"$set":{"name":''.join(outStr.split())}})
                #fout.write(''.join(outStr.split())+'\n')
        #fout.close()
        filename = "tt.txt"
        with open(filename) as f:
            mytxt = f.read()
        print (mytxt.strip())
        path_img ="aaa.jpg"
        background_image = np.array(Image.open(path_img))
        wordcloud = WordCloud(font_path="simsun.ttf",max_font_size=100,scale=1.5).generate(mytxt)
        image_colors = ImageColorGenerator(background_image)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    global db
    global sntable
    global table
    table = 'TaoBaoLipstick'
    mconn = MongoClient("mongodb://localhost")
    db = mconn['test']
    db.authenticate('test', 'test')
    wordle().data()
    mconn.close()
