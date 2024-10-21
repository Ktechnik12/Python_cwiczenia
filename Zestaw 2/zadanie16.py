def replace_gvr(line):
    return line.replace("GvR", "Guido van Rossum")

# Test the function
line = "GvR is the creGvRator of Python."
expected_result = "Guido van Rossum is the creGuido van Rossumator of Python."
result = replace_gvr(line)
assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"
print(result)