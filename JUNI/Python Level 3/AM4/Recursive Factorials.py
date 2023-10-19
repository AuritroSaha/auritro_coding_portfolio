def factorials(n):
    if n == 1:
        return n

    return factorials(n - 1) * n


print(factorials(5))