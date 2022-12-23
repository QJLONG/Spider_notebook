import requests
import asyncio
from bs4 import BeautifulSoup
import re


# 1.获取所有皮肤ID
def main():
    resp = requests.get('https://pvp.qq.com/web201605/herolist.shtml')
    resp.encoding = 'gbk'
    soup = BeautifulSoup(resp.text, 'html.parser')
    ul = soup.find('ul', attrs={'class': 'herolist clearfix'})
    # 2.拼接皮肤IDURL
    lis = ul.find_all('li')
    tasks = []
    for li in lis:
        # print(li)
        pic_id = re.search(r"herodetail/(.*?).shtml", str(li)).group(1)
        for i in range(1, 10):
            pic_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{pic_id}/{pic_id}-bigskin-{i}.jpg'
            pic_name = pic_url.rsplit('/')[-1]
            resp = requests.get(pic_url)
            if resp:
                resp.encoding = 'gbk'
                with open('./data/' + pic_name, "wb") as f:
                    f.write(resp.content)
                print(pic_name, 'is over!!')


# 3.发起异步请求，下载图片
# async def aioDownload(url):
#     file_name = url.rsplit('/')[-1]
#     async with aiohttp.ClientSession as session:
#         async with session.get(url) as resp:
#             pic = await resp.read()
#             async with aiofiles.open('./data/' + file_name, mode='wb') as f:
#                 await f.write(pic)


if __name__ == '__main__':
    main()