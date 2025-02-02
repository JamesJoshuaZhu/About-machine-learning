from pymongo import MongoClient,ASCENDING, DESCENDING
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from pyecharts import Map, Geo
def pandas_data():
    a = db[table].find()
    data = pd.DataFrame(list(a))
    pd.set_option('display.width', None)
    #print (data)
    del data["_id"]
    pd.set_option('display.width', None)
    address = data[["address","People_buy"]]
    province_dis ={}
    for i in range(0,len(address)):
        addresss = address.iat[i,0].split(" ")[0]
        num = address.iat[i,1]
        province_dis[addresss] = num
    print(province_dis)
    shop_keys=province_dis.keys()
    shop_values=province_dis.values()
    map = Map("shop distribution", "@James Zhu",width=1200, height=600)
    map.add("", shop_keys, shop_values, maptype='china', is_visualmap=True,
    visual_text_color='#000')
    map.render(path="shop distribution.html")
def Maps():
    #好友分布图
    province_distribution = {'河南': 45, '北京': 97, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1, '其他': 1}

    province_keys=province_distribution.keys()
    province_values=province_distribution.values()

    map = Map("我的微信好友分布", "@SilenceYaung",width=1200, height=600)
    map.add("", province_keys, province_values, maptype='china', is_visualmap=True,
    visual_text_color='#000')
    map.render()
    #PM2.5分析
    # 空气质量评分
    indexs = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安', '郑州', '重庆', '长沙']
    values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1, 1.31, 3.92, 4.47, 2.40, 3.60]
     
     
    geo = Geo("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
     
    # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
    geo.add("空气质量评分", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[0, 5],visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
    geo.show_config()
    geo.render(path="./data/04-05空气质量评分.html")

    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr= ["China", "Canada", "Brazil", "Russia", "United States"]
     
    # 省和直辖市
    province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1, '其他': 1}
    provice=list(province_distribution.keys())
    values=list(province_distribution.values())
     
    # 城市 -- 指定省的城市 xx市
    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市', '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]
     
    # 区县 -- 具体城市内的区县  xx县
    quxian = ['夏邑县', '民权县', '梁园区', '睢阳区', '柘城县', '宁陵县']
    values3 = [3, 5, 7, 8, 2, 4]

    map0 = Map("世界地图示例", width=1200, height=600)
    map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
    map0.render(path="aa.html")

    #热力分布图
    data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
    ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)]
     
    attr, value = geo.cast(data)
     
    geo = Geo("全国主要城市空气质量热力图", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
     
    geo.add("空气质量热力图", attr, value, visual_range=[0, 25], type='heatmap',visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
    geo.show_config()
    geo.render(path="./data/04-04空气质量热力图.html")

    # maptype='china' 只显示全国直辖市和省级
    # 数据只能是省名和直辖市的名称
    map = Map("中国地图",'中国地图', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 50],  maptype='china', is_visualmap=True,
        visual_text_color='#000')
    map.show_config()
    map.render(path="./data/04-01中国地图.html")

    # 河南地图  数据必须是省内放入城市名
    map2 = Map("河南地图",'河南', width=1200, height=600)
    map2.add('河南', city, values2, visual_range=[1, 10], maptype='河南', is_visualmap=True, visual_text_color='#000')
    map2.show_config()
    map2.render(path="./data/04-02河南地图.html")

    # # 商丘地图 数据为商丘市下的区县
    map3 = Map("商丘地图",'商丘', width=1200, height=600)
    map3.add("商丘", quxian, values3, visual_range=[1, 10], maptype='商丘', is_visualmap=True,
        visual_text_color='#000')
    map3.render(path="./data/04-03商丘地图.html")




if __name__ == "__main__":
    global db
    global sntable
    global table
    table = 'TaoBaoLipstick'
    mconn = MongoClient("mongodb://localhost")
    db = mconn['test']
    db.authenticate('test', 'test')
    pandas_data()
    #Maps()
    mconn.close()
