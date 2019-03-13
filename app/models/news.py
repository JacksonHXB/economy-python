'''
Created on 2019年3月11日

@author: Administrator
'''
from ..__init__ import mongo
print(mongo.db)

db = mongo.db

class News():
    
    
    @staticmethod
    def getNewsList():
        cursor = db.tb_gdp.find().limit(1)
        return cursor
