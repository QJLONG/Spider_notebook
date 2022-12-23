# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 现在改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高。

def consumer():
    print("[CONSUMER] start:")
    r = 'start'
    while True:
        n = yield r
        if not n:
            print("n is empty!")
            continue
        print("[CONSUMER] consumer is consuming ", n)
        r = "200 OK!"


def producer(c):
    print("[PRODOCer] start:")
    start_value = c.send(None)
    print(start_value)
    n = 0
    while n < 3:
        n += 1
        print("[PRODUCER] producer is producing", n)
        r = c.send(n)
        print("[PRODUCER] consumer returned ", r)
    c.close()


c = consumer()
producer(c)
