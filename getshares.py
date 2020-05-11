# @Time : 2020/4/7 0007 14:11 

# @Author : ztrxRestful

# @File : getshares.py 

# @Software: PyCharm


import requests
import json

class getshares():
    def __init__(self):
        file = open(r'setting.properties')
        self.msg_list = file.readlines()
        print(self.msg_list)

    def git_gupiao(self):
        res_list = []
        for id in self.msg_list:
            id = id.replace('\n','')
            if str(id[0:1]) == '0':
                id = '0.' + id
            elif str(id[0:1]) == '6':
                id = '1.' + id
            elif str(id[0:1]) == '3':
                id = '0.' + id
            print(id)
            url = 'http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&fltt=2&fields=f59,f169,f170,f161,f163,f171,f126,f168,f164,f78,f162,f43,f46,f44,f45,f60,f47,f48,f49,f84,f116,f55,f92,f71,f50,f167,f117,f85,f84,f58,f57,f86,f172,f108,f118,f107,f164,f177&invt=2&secid=' + id + '&cb=jQuery112409993007715632225_1585106518099&_=1585106518129'
            res = requests.get(url)
            string = res.text
            string = string[string.find('(') + 1:-2]

            json_res = json.loads(string)
            data = json_res.get('data')
            # print(data)
            # print(data.get('f58'))
            # 股票名字
            name = data.get('f58')
            # 股票编号
            id = data.get('f57')
            # 开盘
            open_amt = data.get('f46')
            # 最高
            max_amt = data.get('f44')
            # 最低
            min_amt = data.get('f45')
            # 现时成交价
            current_amt = data.get('f43')
            # 成交量
            turnover = data.get('f47')
            # 成交额
            business = data.get('f48')
            # 涨跌价
            yuan = data.get('f169')
            # 涨跌幅
            fu = data.get('f170')
            # 昨日收盘
            over_amt = data.get('f60')
            if current_amt > over_amt:
                col = 'red'
            elif current_amt == over_amt:
                col = 'black'
            else:
                col = 'green'
            temp  = [name, id, current_amt, open_amt, max_amt, min_amt, over_amt, turnover, business, yuan, fu, col]
            res_list.append(temp)
        return res_list

# if __name__ == '__main__':
#     # string = '\u4e2d\u8fdc\u6d77\u80fd'
#     # #string = string.decode().encode('unicode_escape')
#     # print(string)
#     shares = getshares()
#     print(shares.git_gupiao())