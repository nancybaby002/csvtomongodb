# coding: utf-8
import csv
from pymongo import MongoClient
URI = "mongodb://192.168.1.160"
PORT = 27017
DB = "taobao"


def connection():
    client = MongoClient(URI, PORT, maxPoolSize=200, connectTimeoutMS=60 * 1000, socketTimeoutMS=60 * 1000)
    db = client[DB]
    return db

db=connection()
# db["itemlist"].drop()
reader=csv.reader(open('qiaokeli.csv', 'rb'))

for item in reader:
    itemid=item[0].decode("gbk").encode("utf-8")
    itemname=item[1].decode("gbk")
    print itemid
    print itemname
    db["itemlist"].insert({"itemid":itemid,"itemname":itemname,"type":"qiaokeli"})