line = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum."""

words = line.split()

total_length = sum(len(word) for word in words)

print("Łączna długość wyrazów w napisie:", total_length)
result = total_length
expected_result = 377

assert result == expected_result, f"Expected {expected_result}, but got {result}"
print("Test zaliczony.")