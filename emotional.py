from snownlp import SnowNLP
text="皱皱的颜色。也不鲜艳。很喜欢。但总归。还是嫌弃。"
s = SnowNLP(text)
for i in s.sentences:
    #print(i)
    s1 = SnowNLP(i)
    #print(s1.sentiments)
text="皱皱的颜色也不鲜艳很喜欢但总归还是嫌弃"
a = SnowNLP(text)
print(text)
print(a.sentiments)
text="皱皱的颜色也不鲜艳很嫌弃但总归还是喜欢"
a = SnowNLP(text)
print(text)
print(a.sen timents)
