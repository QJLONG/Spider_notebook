# 生成器（Generator）
# 1.yield的使用

def test():
    print("#Generator Start:")
    n = 1
    while True:
        generate_expression_value = yield n
        print("#generate_expression_value:", generate_expression_value)
        n += 1


# 带有yield的函数将不再是一个函数，它会返回一个生成器对象
generator = test()
print(type(generator))

# 启动生成器：
result1 = generator.__next__()
print("#result1:", result1)  # 可以发现，生成器启动后，会执行到yield处发生中断，返回结果是yield表达式的值

# 再次启动生成器：generator.__next__()等效于generator.send(None)
result2 = generator.send(666)
print("#result2:", result2)  # 再次启动时，从上次中断处开始执行，并将send的参数赋值给yield表达式
