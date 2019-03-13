'''
Created on 2019年3月11日

@author: Administrator
'''
from flask import Flask
from flask_pymongo import PyMongo
from app.views import indexController
from app.views import stockController
from app.views import newsController


app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/db_finance"
mongo = PyMongo(app)

# 注册蓝图管理路由系统
app.register_blueprint(indexController, url_prefix="/")                 # 优先级更高
app.register_blueprint(stockController, url_prefix="/stock")            # 访问该路由的时候需要添加前缀
app.register_blueprint(newsController, url_prefix="/news")  



def init_system():
    return app