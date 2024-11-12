from math import gcd

def simplify(frac):
    numerator, denominator = frac
    divisor = gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]

def add_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    return simplify([numerator, denominator])

def sub_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    return simplify([numerator, denominator])

def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return simplify([numerator, denominator])

def div_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    return simplify([numerator, denominator])

def is_positive(frac):
    return frac[0] * frac[1] > 0

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    diff = sub_frac(frac1, frac2)
    if diff[0] > 0:
        return 1
    elif diff[0] < 0:
        return -1
    return 0

def frac2float(frac):
    return frac[0] / frac[1]
