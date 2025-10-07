def Special_Pythagorean_Triplet(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return None
print(Special_Pythagorean_Triplet(1000))