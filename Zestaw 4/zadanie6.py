def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (int, float)):
            total += item
        else:
            raise ValueError("Sequence can only contain integers, floats, lists, or tuples.")
    return total

assert sum_seq([1, 2, (3, 4), [5, 6]]) == 21
assert sum_seq([1, [2, [3]], 4]) == 10
assert sum_seq([1, (2, [3, (4, 5)]), 6]) == 21
print("Wszystkie testy zaliczone!")