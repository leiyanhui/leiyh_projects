# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect()

cursor = conn.cursor()

cursor.execute()

cursor.close()
conn.close()

import pymongo

client = pymongo.MongoClient()

db = client.myDb  # myDb 为数据库名

# 执行数据库的语句





