import asyncio


# async def compute(x, y):
#     print("Compute %s+%s is ..." % (x, y))
#     await asyncio.sleep(1.0)
#     return x+y
#
#
# async def print_sum(x, y):
#     result = await compute(x, y)
#     print("%s+%s=%s" % (x, y, result))
#
#
# async def print_test():
#     print("test123")
#
#
# loop = asyncio.get_event_loop()
# print("start")
# loop.run_until_complete(asyncio.wait([
#     print_sum(1, 2),
#     print_test()
# ]))
# print("end")
# loop.close()


future = asyncio.Future()


async def coro1():
    print("wait 1 second:")
    await asyncio.sleep(1.0)
    print("set_result")
    future.set_result("data")


async def coro2():
    print("coro2")
    result = await future
    print(result)


async def coro3():
    print("coro3")


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    coro2(),
    coro1()
]))