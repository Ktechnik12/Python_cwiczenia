
#wersja interacyjna
def odwracanie(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        raise ValueError("Invalid left or right indices.")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L


assert odwracanie([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
assert odwracanie([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1]
assert odwracanie([1, 2, 3, 4, 5], 0, 0) == [1, 2, 3, 4, 5]
print("Wszystkie testy iteracyjne zaliczone!")

#wersja rekurencyjna
def odwracanie_recursive(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        raise ValueError("Invalid left or right indices.")
    if left >= right:
        return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_recursive(L, left + 1, right - 1)

assert odwracanie_recursive([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]
assert odwracanie_recursive([1, 2, 3, 4, 5], 0, 4) == [5, 4, 3, 2, 1]
assert odwracanie_recursive([1, 2, 3, 4, 5], 0, 0) == [1, 2, 3, 4, 5]
print("Wszystkie testy rekurencyjne zaliczone!")