'''
Created on 2019年3月11日

@author: Administrator
'''
from flask import Response
import json
from . import newsController
from app.service import newsService
from bson import json_util



NewsService = newsService.NewsService()


# springcloud检测该服务是否运行的接口
@newsController.route("/list")
def newsList():
    result = NewsService.getNews()
    return Response(json_util.dumps(result))

