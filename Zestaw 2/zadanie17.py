def sort_words(line):
    words = line.split()
    sorted_alphabetically = sorted(words)
    sorted_by_length = sorted(words, key=len)
    return sorted_alphabetically, sorted_by_length

line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
expected_result_alphabetically = ['Lorem', 'adipiscing', 'amet,', 'consectetur', 'dolor', 'elit', 'ipsum', 'sit']
expected_result_by_length = ['sit', 'elit', 'Lorem', 'ipsum', 'dolor', 'amet,', 'adipiscing', 'consectetur']

result_alphabetically, result_by_length = sort_words(line)

assert result_alphabetically == expected_result_alphabetically, f"Expected {expected_result_alphabetically}, but got {result_alphabetically}"
assert result_by_length == expected_result_by_length, f"Expected {expected_result_by_length}, but got {result_by_length}"

print("Posortowane alfabetycznie:", result_alphabetically)
print("POsortowane po dlugości:", result_by_length)