def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
    return num
print(nth_prime(10001))