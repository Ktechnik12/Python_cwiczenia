def count_words(multiline_string):
    words = multiline_string.split()
    return len(words)

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
word_count = count_words(line)
print(f"Ilosc slow: {word_count}")
expected_result = 69
assert word_count == expected_result, f"Expected {expected_result}, but got {word_count}"
print("Test zaliczony.")
