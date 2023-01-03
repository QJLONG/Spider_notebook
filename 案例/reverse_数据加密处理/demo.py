'''
Description: 
Language: UTF-8
Author: hummer
Date: 2022-12-30 17:06:34
'''
import requests
import time
import execjs

cookies = {
    'ASP.NET_SessionId': 'wii4iodjkzqtsttshas0sbve',
}

json_data = {
    'pageNo': 1,
    'pageSize': 20,
    'total': 0,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-06-30 00:00:00',
    'EndTime': '2022-12-30 23:59:59',
    'createTime': [],
    'ts': round(time.time() * 1000),
}

portal_sign = execjs.compile(open(".\\头部签名逆向.js", 'r', encoding='utf-8').read()).call('d', json_data)
# print(portal_sign)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=wii4iodjkzqtsttshas0sbve',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'portal-sign': portal_sign,
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo', cookies=cookies, headers=headers, json=json_data).json()
data = response['Data']
result = execjs.compile(open(".\\数据逆向.js", 'r', encoding='utf-8').read()).call("b", data)
print(result)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pageNo":1,"pageSize":20,"total":0,"AREACODE":"","M_PROJECT_TYPE":"","KIND":"GCJS","GGTYPE":"1","PROTYPE":"","timeType":"6","BeginTime":"2022-06-30 00:00:00","EndTime":"2022-12-30 23:59:59","createTime":[],"ts":1672390805845}'
#response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo', cookies=cookies, headers=headers, data=data)