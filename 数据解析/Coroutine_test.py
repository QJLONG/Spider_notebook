import asyncio
import requests
import aiohttp
from lxml import etree
import re
import aiofiles

url = "https://pvp.qq.com/web201605/herolist.shtml"
resp = requests.get(url)
tree = etree.HTML(resp.text)
hrefs = tree.xpath('//ul[@class="herolist clearfix"]/li/a/@href')
urls = ['https://pvp.qq.com/web201605/' + href for href in hrefs]


# 异步获取所有html
async def fetch(curl):
    conn = aiohttp.TCPConnector(limit=3)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(curl) as resp:
            html = await resp.text()
            return html


async def fetch_multi(curls):
    tasks = []
    for curl in curls:
        task = asyncio.create_task(fetch(curl))
        tasks.append(task)
    htmls = await asyncio.gather(*tasks)
    return htmls


def get_img_urls(htmls):
    # 获取每个html页面中的所有图片url
    img_urls = []
    for html in htmls:
        tree = etree.HTML(html)
        temp1 = tree.xpath("//div[@class='zk-con1 zk-con']/@style")
        temp2 = tree.xpath("//div[@class='pic-pf']/ul/@data-imgname")[0]
        skins = str(temp2).split("|")
        h_id = re.search(r"background:url\('.*?/hero-info/(\d+)/.*?-bigskin-.*?.jpg'\).*?", temp1[0], re.S).group(1)
        for i in range(len(skins)):
            img_url = f'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{h_id}/{h_id}-bigskin-{i+1}.jpg'
            img_urls.append(img_url)
    return img_urls


# 异步下载图片
async def aioDownload(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            pic_name = url.rsplit("/")[-1]
            async with aiofiles.open("../data/" + pic_name, 'wb') as f:
                await f.write(content)
                print(pic_name, "downloading...")


async def aio_down_multi(img_urls):
    tasks = []
    for img_url in img_urls:
        task = asyncio.create_task(aioDownload(img_url))
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # 异步获取所有html
    loop = asyncio.get_event_loop()
    task = loop.create_task(fetch_multi(urls))
    loop.run_until_complete(task)
    htmls = task.result()

    # 异步下载所有图片
    img_urls = get_img_urls(htmls)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio_down_multi(img_urls))
    print("Over!")

