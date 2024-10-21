def find_longest_word(line):
    words = line.split()
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

line = "Znaleźć najdłuższy wyraz w tym napisie"
expected_result = ("najdłuższy", 10)
result = find_longest_word(line)
assert result == expected_result, f"Expected {expected_result}, but got {result}"
print(result)

line = "To jest testowy napis"
expected_result = ("testowy", 7)
result = find_longest_word(line)
assert result == expected_result, f"Expected {expected_result}, but got {result}"
print(result)

print("Testy zaliczony.")