def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
print("Wszystkie testy zaliczone!")