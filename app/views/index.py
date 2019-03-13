'''
首页的路由管理
'''
from flask import Response
import json
from . import indexController



# springcloud检测该服务是否运行的接口
@indexController.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype="application/json")



@indexController.route("/test")
def test():
    return "test"


























