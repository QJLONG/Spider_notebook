# 环境搭建：
#     pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
#     下载浏览器驱动：
#     谷歌浏览器 chromedrive：http://chromedriver.storage.googleapis.com/index.html
#     火狐浏览器 geckodriver：https://github.com/mozilla/geckodriver/releases
#     IE 浏览器 IEDriver：http://selenium-release.storage.googleapis.com/index.html
#     将下载好的驱动放在python解释器所在文件夹即可
#让selenium启动Chrome浏览器
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# 1.创建浏览器对象
web = Chrome()
# 2.打开一个网址
web.get("http://lagou.com")
print(web.title)
# 找到元素，点击
el = web.find_element(By.XPATH, r'//*[@id="changeCityBox"]/p[1]/a')
# print(type(el)) <class 'selenium.webdriver.remote.webelement.WebElement'>
el.click()
time.sleep(1)
# 找到搜索框，输入python，按回车
search = web.find_element(By.XPATH, r'//*[@id="search_input"]')
search.send_keys("python", Keys.ENTER)
# 获取所有岗位信息的div
divs = web.find_elements(By.XPATH, r'//*[@id="jobList"]/div[1]/div')
datas = []
for div in divs:
    datas.append([])
    job_name = div.find_element(By.XPATH, r'./div/div/div/a').text
    # print(job_name)
    datas[-1].append(job_name)
    job_time = div.find_element(By.XPATH, r'./div/div/div/span').text
    # print(job_time)
    datas[-1].append(job_time)
    job_price = div.find_element(By.XPATH, r'./div/div/div[2]/span').text
    # print(job_price)
    datas[-1].append(job_price)
    job_req = div.find_element(By.XPATH, r'./div/div/div[2]').text
    # print(job_req)
    datas[-1].append(job_req)
    time.sleep(0.5)

# 将获取到的数据写入CSV文件
f = open("python_data.csv", mode='w', encoding="utf-8")
csv_writer = csv.writer(f)
for data in datas:
    csv_writer.writerow(data)
f.close()
print("存储完成！！！")


