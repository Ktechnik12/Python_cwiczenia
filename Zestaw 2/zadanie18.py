def count_zeros(number):
    return str(number).count('0')

number = 10020030000098643679987604
result = count_zeros(number)
expected_result = 10
assert result == expected_result, f"Expected {expected_result}, but got {result}"

print(f"Ilość zer w liczbie {number} to: {result}")