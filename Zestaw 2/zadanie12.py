def first_and_last_characters(line):
    words = line.split()
    first_chars = ''.join(word[0] for word in words)
    last_chars = ''.join(word[-1] for word in words)
    return first_chars, last_chars

line = "Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line"
first_chars, last_chars = first_and_last_characters(line)
print("Pierwsze znaki:", first_chars)
print("Ostatnie znaki:", last_chars)
expected_first_chars = "Znszpzwzwl"
expected_last_chars = "ćsyzhwwzae"
assert first_chars == expected_first_chars, f"Expected {expected_first_chars}, but got {first_chars}"
assert last_chars == expected_last_chars, f"Expected {expected_last_chars}, but got {last_chars}"
print("Test zaliczony.")

