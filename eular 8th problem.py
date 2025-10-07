def Largest_Product_in_a_Series(n, k):
    digits = [int(d) for d in str(n)]
    max_product = 0
    for i in range(len(digits) - k + 1):
        product = 1
        for j in range(k):
            product *= digits[i + j]
        if product > max_product:
            max_product = product
    return max_product
