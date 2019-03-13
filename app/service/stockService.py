

import tushare as ts            # 导入tushare金融数据包



class stockService(object):
    
    @staticmethod
    def getStockList():
        df = ts.get_realtime_quotes('000581')
        print(df)
        return None
    
    
    # 获取实时分笔数据
    @staticmethod
    def getSplitData(code):
        print(code)
        df = ts.get_realtime_quotes(code)
        for row in df.iterrows():
            print(row)


        return df
    



















