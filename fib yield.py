def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 生成斐波那契数列的前10个数字
n = 10
fibonacci_sequence = list(fib(n))
print(f"Fibonacci sequence of {n} numbers: {fibonacci_sequence}")
