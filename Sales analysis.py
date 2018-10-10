from pymongo import MongoClient,ASCENDING, DESCENDING
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
def pandas_data():
    a = db[table].find()
    data = pd.DataFrame(list(a))
    del data["_id"]
    pd.set_option('display.width', None)
    #print(data)
    list_People = []
    list_name=[]
    df = data[["People_buy","shop"]]
    #print(df)
    #print(len(df))
    for i in range(0,len(df)):
        num = (df.iat[i,0])
        name = df.iat[i  ,1]
        list_name.append(name)
        list_People.append(int(num)/10000)
    print(list_name)
    plt.rcParams['font.sans-serif'] = ['SimHei'] 
    plt.rcParams['font.family']='sans-serif'
    x =np.arange(len(list_name))
    fig,ax = plt.subplots()
    b = ax.bar(x,list_People,color='k', alpha=0.8,tick_label=list_name)
    #print(type(b))
    #datas = pd.Series(list_People, index=list_name)
    #c = datas.plot.bar(color='k', alpha=0.8) # 垂直柱状图
    #print(type(c))
    for i in b:
        h = i.get_height()
        ax.text(i.get_x()+i.get_width()/2,h,'%.4f'%h,ha='center',va='bottom')
    plt.xticks(rotation=15)
    plt.xlabel("店铺名称")
    plt.ylabel("购买人数/10000")
    plt.title("销售分析")
    plt.ylim(0,10)
    plt.show()

    
if __name__ == "__main__":
    global db
    global sntable
    global table
    table = 'TaoBaoLipstick'
    mconn = MongoClient("mongodb://localhost")
    db = mconn['test']
    db.authenticate('test', 'test')
    pandas_data()
    mconn.close()
