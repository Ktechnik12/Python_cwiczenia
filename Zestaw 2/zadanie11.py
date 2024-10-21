word = "Python"
result = "_".join(word)
print(result)
expected_result = "P_y_t_h_o_n"
assert result == expected_result, f"Expected {expected_result}, but got {result}"
print("Test zaliczony.")