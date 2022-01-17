def multi_n(n):
    r = 0
    for i in range(1, n + 1):
        r = r + (i * i)
    return r


def multi_n2(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(multi_n(10))  # O(n)
print(multi_n2(10)) # O(1)

