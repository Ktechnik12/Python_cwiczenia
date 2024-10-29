def rysuj_miarke(dlugosc):
    miarka = '|' + '|'.join(['....'] * dlugosc) + '|\n'
    numeracja = ''.join([f"{i:<5}" for i in range(dlugosc + 1)])
    return miarka + numeracja

print(rysuj_miarke(12))
