def znajdz_wspolne_i_unikalne(sekwencja1, sekwencja2):
    wspolne = list(set(sekwencja1) & set(sekwencja2))
    wszystkie = list(set(sekwencja1) | set(sekwencja2))
    return wspolne, wszystkie

seq1 = [1, 2, 3, 4]
seq2 = [3, 4, 5, 6]
expected_result = ([3, 4], [1, 2, 3, 4, 5, 6])
result = znajdz_wspolne_i_unikalne(seq1, seq2)
assert result == expected_result, "Test nie przeszedł"
print(result)
