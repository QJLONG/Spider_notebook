# 协程:程序要到IO操作并被阻塞时，CPU转而执行其他部分程序，即多任务操作
import asyncio
import time


# async def func():
#     print("你好啊，我叫赛利亚")
#
#
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数，执行得到的是一个协程对象
#     # print(g) # <coroutine object func at 0x0000013F841ADDC0>
#     asyncio.run(g)

# async def func1():
#     print("你好啊，我叫潘金莲")
#     # time.sleep(3)   # time.sleep()是一个同步操作，它会使异步操作中断
#     await asyncio.sleep(3)    # 异步操作的睡眠
#     print("你好啊，我叫潘金莲")
#
#
# async def func2():
#     print("你好啊，我叫王建国")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊，我叫王建国")
#
#
# async def func3():
#     print("你好啊，我叫李雪琴")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好啊，我叫李雪琴")
#
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     # 一次性启动多个协程任务
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)


async def func1():
    print("你好啊，我叫潘金莲")
    # time.sleep(3)   # time.sleep()是一个同步操作，它会使异步操作中断
    await asyncio.sleep(3)  # 异步操作的睡眠
    print("你好啊，我叫潘金莲")


async def func2():
    print("你好啊，我叫王建国")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("你好啊，我叫王建国")


async def func3():
    print("你好啊，我叫李雪琴")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("你好啊，我叫李雪琴")


# 规范写法
async def main():
    # 第一种写法：
    # f1 = func1()
    # await f1
    # 第二种写法（推荐）
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2-t1)