def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5
assert fibonacci(10) == 55
print("Wszystkie testy zaliczone!")
