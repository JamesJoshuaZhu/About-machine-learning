import requests
from bs4 import BeautifulSoup
import time
import json
import re
from pymongo import MongoClient,ASCENDING, DESCENDING
def TaoBao():
    url = "https://s.taobao.com/api?_ksTS=1536909846924_354&callback=jsonp355&ajax=true&m=customized&sourceId=tb.index&bcoffset=-1&commend=all&sort=default&ssid=s5-e&search_type=item&q=口红&spm=a21bo.2017.201856-taobao-item.1&s=36&imgfile=&initiative_id=tbindexz_20170306&ie=utf8&rn=dbce0ef7de2715ed68520d0d783077e3"
    headers={"authority": "s.taobao.com",
"method": "GET",
"path": "/api?_ksTS=1536909447974_254&callback=jsonp255&ajax=true&m=customized&sourceId=tb.index&bcoffset=0&commend=all&ssid=s5-e&search_type=item&spm=a230r.1.1998181369.d4919860.4a353f34ONB9fa&q=%E5%8F%A3%E7%BA%A2&s=32&tab=mall&imgfile=&initiative_id=tbindexz_20170306&ie=utf8&rn=46d3ea0b0f03d20656f703380c418af4",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"cache-control": "max-age=0",
"cookie": "cna=/aHyE2BVpRICAQuNoGeo97+j; t=69c36a9934f18133245952fa28a90e21; _m_h5_tk=b4680c8d12ef053d88106b8d705f4fec_1536906590267; _m_h5_tk_enc=110db4dcd1381a0c1524d479d9c7bff9; cookie2=19991ededd31fe834eb59c8d39e0573e; _tb_token_=5b6391ef15704; enc=JMNrrb5N0eOh33WovleVspm6jyEQROBTgy53XwxWHjmF%2BEs9SUk2%2FheFTLhz4EKp0p0ahDaiQAnrFO69gn0riA%3D%3D; v=0; thw=cn; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=241DB7A422C617F89EE4756A732D9E2B; isg=BDQ0YmaE0_wqpkcwUehgqTtQBfJmpVmHhWqju86VwL9DOdSD9h0oh-r_vTFE2pBP",
"referer": "https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.4a353f34ONB9fa&q=%E5%8F%A3%E7%BA%A2&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&ie=utf8&initiative_id=tbindexz_20170306&tab=mall",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
    r = requests.get(url,headers = headers,timeout=20)
    h = r.text.replace("jsonp355(","").replace(");","")
    dt = json.loads(h)
    a = dt.get("API.CustomizedApi").get("itemlist").get("auctions")
    #print (a)
    data={}
    for i in a:
        lipstickurl = 'https:'+i.get("detail_url")
        data["lipstickurl"] = lipstickurl
        shop = i.get("nick")
        data["shop"] = shop
        address = i.get("item_loc")
        data["address"] = address
        price = i.get("view_price")
        data["price"] = price
        name = i.get("title")
        data["name"] = name
        People_buy = i.get("view_sales").replace("人付款","")
        data["People_buy"] = People_buy
        #print (lipstickurl)
        #print(People_buy)
        #time.sleep(10)
        data_db(data)
def data_db(data):
      count = db[table].find({'lipstickurl':data.get("lipstickurl")}).count()
      if count <= 0:
        sn = getNewsn()
        db[table].insert({"sn":sn})
        db[table].update({'sn':sn},{'$set':data})
        print (str(sn) + ' inserted successfully')
        time.sleep(1.5)
      else:
        print('url exist')
def getNewsn():    
    db.sn.find_and_modify({"_id": table}, update={ "$inc": {'currentIdValue': 1}},upsert=True)
    dic = db.sn.find({"_id":table}).limit(1)
    return dic[0].get("currentIdValue")
if __name__ == "__main__":
    global db
    global sntable
    global table
    table = 'TaoBaoLipstick'
    mconn = MongoClient("mongodb://localhost")
    db = mconn['test']
    db.authenticate('test', 'test')
    TaoBao()
