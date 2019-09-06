# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import redis
from scrapy.conf import settings
from AIHR.items import AihrItem, CompanyItem, QcwyPostItem, QcwyCompanyItem

class AihrPipeline(object):

    def __init__(self):
        # #连接数据库
        host = settings["MONGO_HOST"]
        port = settings["MONGO_PORT"]
        dbname = settings["MONGO_DB"]
        sheetname = settings["MONGO_COLLPO"]
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        # mydb.authenticate(user, pwd)
        self.post = mydb[sheetname]
        # self.comp = mydb[mycoll]

        self.redis_url = 'redis://localhost:6379/'
        self.r = redis.Redis(host="localhost", port=6379)

    def process_item(self, item, spider):
        # data = dict(item)  # 把item转化成字典形式
        # print("+++++++++++++++++++")
        # if isinstance(item, (AihrItem, QcwyPostItem)):
        #     self.post.update({'postName': item['postName'], 'companyName': item['companyName'],
        #                       'address': item['address']}, {'$set': data}, upsert=True)  # 向数据库插入一条记录
        # return item  # 会在控制台输出原item数据，可以选择不写

        self.r.lpush('hyperchain:start_urls', item['url'])

