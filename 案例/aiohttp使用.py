import aiohttp
import asyncio


urls = [
    "https://www.umei.cc/d/file/20221109/8c45f80641a1f63bd733be8fe8980551.jpg",
    "https://www.umei.cc/d/file/20221109/3d2520db7ae7be0d17b101f4639b51f4.jpg",
    "https://www.umei.cc/d/file/20221109/20cf090e501878d0dfa3e7f3fdd84be8.jpg"
]


async def download(url):
    file_name = url.rsplit('/', 1)[1]
    # 发送请求
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # 写入文件
            with open(file_name, "wb") as f:
                f.write(await resp.content.read())
    print(file_name, "搞定!")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
