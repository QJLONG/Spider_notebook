# 进程->资源单位
# 线程->执行单位

from threading import Thread


# def func():
#     for i in range(1000):
#         print("func",i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)     # 创建线程并给线程安排任务
#     t.start()   # 多线程状态为可以开始执行状态，具体执行时间有CPU决定
#     for i in range(1000):
#         print("main", i)

# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("子线程", i)
#
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
#
#     for i in range(1000):
#         print("主线程", i)


# 线程池的使用
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")

    print("123")
