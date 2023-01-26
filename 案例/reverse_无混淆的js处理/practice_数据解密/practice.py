'''
Description: 
Language: UTF-8
Author: hummer
Date: 2023-01-04 22:24:15
'''
import requests

headers = {
    'Accept': "application/json, text/plain, */*",
    'Content-Type': "application/x-www-form-urlencoded"
}

resp = requests.get("https://www.qimingpian.com/finosda/project/pinvestment", headers=headers)
resp.encoding = 'utf-8'

print(resp.text)