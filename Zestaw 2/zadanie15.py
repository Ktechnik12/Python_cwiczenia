def concatenate_digits(L):
    return ''.join(str(num) for num in L)

L = [12, 34, 56,78,9,0]
result = concatenate_digits(L)
expected_result = "1234567890"
assert result == expected_result, f"Expected {expected_result}, but got {result}"
print(result)