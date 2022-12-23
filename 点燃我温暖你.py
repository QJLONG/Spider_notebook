# https://new.qqaku.com/20221103/LFK4ySf2/index.m3u8
# /20221103/LFK4ySf2/1100kb/hls/index.m3u8
# 爬取目标：https://wujicloud.cn/vodplay/42879-1-1.html
# 操作步骤：
# 1.页面源代码中获取第一层m3u8文件
# 2.从下载下来的m3u8文件中获取第二层m3u8文件
# 3.异步下载所有ts文件
# 4.合并所有ts文件为mp4文件
import os
import requests
import re
import asyncio
import aiofiles
import aiohttp


def download_m3u8(m3u8_url, name):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    resp = requests.get(m3u8_url, headers=headers)
    # print(resp.status_code)
    with open(name, "wb") as f:
        f.write(resp.content)


def get_first_m3u8_url(url):
    resp = requests.get(url)
    re_obj = re.compile(r'"url":"(.*?)",', re.S)
    return re_obj.findall(resp.text)[1].replace(r"\/", r"/")


def get_second_m3u8_url(name):
    with open(name, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()
                # print(line)
                return str(line)


async def aio_download(ts_url, session):
    ts_name = ts_url.split("/")[-1]
    # print(ts_name, "下载中...")
    async with session.get(ts_url) as resp:
        # print(resp.status)
        async with aiofiles.open("./data2/" + ts_name, mode="wb") as f:
            await f.write(await resp.content.read())
            print(ts_name, "下载完毕！")


async def download_ts(name):
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(name, mode="r", encoding='utf-8') as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                else:
                    line = line.strip()
                    tasks.append(asyncio.create_task(aio_download(line ,session)))
            completed, pending = await asyncio.wait(tasks, timeout=40)
            if pending:
                for i in pending:
                    print("canceling tasks")
                    i.cancel()


def merge_ts(name):
    names = []
    with open(name, mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()
                name = line.split("/")[-1]
                names.append(name)

    res = os.popen(f"cd data2 & copy /b {names[0]}+{names[1]} result.mp4")
    # print(f"copy /b {names[0]}+{names[1]} result.mp4")
    # print(res.read())
    for name in names[2: ]:
        cmd = f"cd data2 & copy /b result.mp4+{name} result.mp4"
        res = os.popen(cmd)
        print(res.read())
    print("ts文件合并完成！")





def main(url):
    domain = "https://new.qqaku.com"
    # 获取第一层m3u8
    # first_m3u8_url = get_first_m3u8_url(url)
    # download_m3u8(first_m3u8_url, "1_first.m3u8")
    # print(first_m3u8_url)
    # 获取第二层m3u8
    # second_m3u8_url = domain + get_second_m3u8_url("1_first.m3u8")
    # download_m3u8(second_m3u8_url, "1_second.m3u8")
    # print(second_m3u8_url)

    # 异步下载ts文件
    # asyncio.run(download_ts("1_second.m3u8"))
    # loop.close()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(download_ts("1_second.m3u8"))
    print("ts下载完毕！")

    # 合并所有ts文件
    merge_ts("1_second.m3u8")


if __name__ == '__main__':
    url = "https://wujicloud.cn/vodplay/42879-1-1.html"
    main(url)