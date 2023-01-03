from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import requests

# 1.获取所有子链接
resp = requests.get('https://pvp.qq.com/web201605/herolist.shtml')
tree = etree.HTML(resp.text,)
ul_tree = tree.xpath('/html/body/div[2]/div/div[3]/ul')
# urls = ul_tree.xpath('./li/a/@href')
print(ul_tree)



# 多线程：
# 2.获取每个子链接的皮肤数量和名称
# 3.下载每个皮肤
