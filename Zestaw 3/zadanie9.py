sekwencje = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
expected_result = [0, 4, 3, 7, 18]
suma_sekwencji = [sum(sekwencja) for sekwencja in sekwencje]
assert suma_sekwencji == expected_result, "Test nie przeszedł"
print(suma_sekwencji)
