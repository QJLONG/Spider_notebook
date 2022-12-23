# 获取各个章节的cid
# 将各个章节的cid和整个小说的gid拼接成url:
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
# 异步操作请求章节内容并保存

import aiohttp
import asyncio
import requests
import aiofiles


async def main():
    # 获取各个章节的cid
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    resp = requests.get(url)
    cids = resp.json()['data']['novel']['items']

    # 将各个章节的cid和整个小说的gid拼接成url
    c_urls = []
    tasks = []
    for cid in cids:
        c_url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|'+ cid['cid']  +'","need_bookinfo":1}'
        tasks.append(asyncio.create_task(aiodownload(c_url)))
    await asyncio.wait(tasks)


# 异步操作请求章节内容并保存
async def aiodownload(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dict = await resp.json()
            c_name = dict['data']['novel']['chapter_title']
            async with aiofiles.open('./novel/' + c_name + '.txt', 'w', encoding='utf-8') as f:
                await f.write(dict['data']['novel']['content'])


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
