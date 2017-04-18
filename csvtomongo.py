# coding: utf-8
import csv
from pymongo import MongoClient
URI = "mongodb://你的地址"
PORT = 你的端口号
DB = "你的数据库名"


def connection():
    client = MongoClient(URI, PORT, maxPoolSize=200, connectTimeoutMS=60 * 1000, socketTimeoutMS=60 * 1000)
    db = client[DB]
    return db

# 连接数据库
db=connection()
reader=csv.reader(open('你的表格文件.csv', 'rb'))
for item in reader:
    # 解析文件中的数据
    itemid=item[0].decode("gbk").encode("utf-8")
    itemname=item[1].decode("gbk")
    # 插入到数据库中
    db["itemlist"].insert({"itemid":itemid,"itemname":itemname,"type":"qiaokeli"})
