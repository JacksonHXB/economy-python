'''
股票的视图函数
'''
from flask import Response
import json
from . import stockController
from ..service.stockService import stockService



@stockController.route("/list")
def getStockList():
    result = stockService.getStockList()
    return Response(result)



@stockController.route("/splitData/<code>", methods=['GET'])
def getSplitData(code):
    result = stockService.getSplitData(code)
    print(result)
    return Response(json.dumps(result))
    



































