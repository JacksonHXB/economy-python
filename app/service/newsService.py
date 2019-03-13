'''
Created on 2019年3月11日

@author: Administrator
'''
from app.models import news
from app.models import respEntity

News = news.News()
RespEntity = respEntity.RespEntity()


class NewsService():
    @staticmethod
    def getNews():
        newsList = News.getNewsList()
        arr = []
        for item in newsList:
            arr.append(item)
        result = RespEntity.getRes(arr)
        return result























