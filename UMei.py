"""
    1. 抓取主页面的源代码，获取子页面的herf
    2. 获取子页面源代码，获取图片连接
    3. 下载图片并保存到本地
"""
import requests
from bs4 import BeautifulSoup
import time

# Get image download link from sub_url
def get_image_link(sub_url):
    resp = requests.get("https://www.umei.cc" + sub_url)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    image_div = soup.find("div", attrs={"class": "big-pic"})
    return image_div.find("img").get("src")


url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"
html = resp.text

soup = BeautifulSoup(html, "html.parser")
div_soup = soup.find("div", attrs={"class": "item_list infinite_scroll"})
images_soup = div_soup.find_all("div", attrs={"class": "item masonry_brick"})
for image_soup in images_soup:
    sub_url = image_soup.find("a").get("href")
    image_link = get_image_link(sub_url)
    # Start to download pictures
    image_resp = requests.get(image_link)
    pic_name = image_link.split('/')[-1]    # get the str behind the last "/"
    with open("./pics/" + pic_name, "wb") as f:
        f.write(image_resp.content)

    print(pic_name+" downlaod over!\n")
    time.sleep(1)




