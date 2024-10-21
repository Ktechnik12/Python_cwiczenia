def format_numbers(L):
    return ''.join(str(num).zfill(3) for num in L)

# Example usage
L = [1, 23, 456, 7, 89,9,11]
result = format_numbers(L)
expected_result = "001023456007089009011"
assert result == expected_result, f"Expected {expected_result}, but got {result}"
print(result)