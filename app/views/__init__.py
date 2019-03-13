'''
Created on 2019年3月11日

@author: Administrator
'''
from flask import Blueprint


indexController = Blueprint('indexController',__name__)
from . import index


stockController = Blueprint('stockController', __name__)
from . import stock


newsController = Blueprint('newsController', __name__)
from . import news


































