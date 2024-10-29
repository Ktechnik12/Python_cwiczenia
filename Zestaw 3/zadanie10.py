# Sposób 1: ręczne przypisanie
roman_to_arabic = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

# Sposób 2: użycie funkcji zip() i dwóch list
litery = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
wartosci = [1, 5, 10, 50, 100, 500, 1000]
roman_to_arabic_zip = dict(zip(litery, wartosci))

# Sposób 3: iterowanie przez listę krotek
roman_to_arabic_tuples = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

# Funkcja tłumacząca liczby rzymskie na arabskie
def roman2int(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_arabic[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Przykładowe dane i testy
expected_result = 14
result = roman2int("XIV")
assert result == expected_result, "Test nie przeszedł dla XIV"

expected_result = 1994
result = roman2int("MCMXCIV")
assert result == expected_result, "Test nie przeszedł dla MCMXCIV"

print("Wynik dla 'XIV':", roman2int("XIV"))
print("Wynik dla 'MCMXCIV':", roman2int("MCMXCIV"))
