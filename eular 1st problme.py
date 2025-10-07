def sum_of_the_multiples_of_3_and_5_below(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

print(sum_of_the_multiples_of_3_and_5_below(1000))