def Even_Fibonacci_sum(n):
    a, b = 0, 1
    even_sum = 0
    while b <= n:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum
